from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

def conectar():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "172.16.0.24"),  # IP do servidor
        database=os.getenv("POSTGRES_DB", "postgres"),
        user=os.getenv("POSTGRES_USER", "sup_cristian"),
        password=os.getenv("POSTGRES_PASSWORD", "17qysrutiov35W"),
        port=int(os.getenv("POSTGRES_PORT", "5432"))
    )

@app.route('/inserir', methods=['POST'])
def inserir_ou_atualizar_pesquisa():
    dados = request.get_json() or {}
    contato = dados.get("contato")

    # Coleta todas as questões dinamicamente (questao1 a questao58)
    questoes = [dados.get(f"questao{i}") for i in range(1, 59)]

    if not contato:
        return jsonify({"erro": "Campo 'contato' é obrigatório"}), 400

    try:
        conn = conectar()
        cur = conn.cursor()

        # Monta dinamicamente a lista de colunas e placeholders
        colunas = ", ".join([f"questao{i}" for i in range(1, 59)])
        placeholders = ", ".join(["%s"] * 58)
        updates = ", ".join([f"questao{i} = COALESCE(EXCLUDED.questao{i}, whuana.questao{i})" for i in range(1, 59)])

        sql = f"""
            INSERT INTO public.whuana AS whuana (
                contato, {colunas}
            )
            VALUES (%s, {placeholders})
            ON CONFLICT (contato) DO UPDATE SET
                {updates};
        """

        cur.execute(sql, [contato] + questoes)
        conn.commit()
        cur.close()
        conn.close()

        return jsonify({"status": "ok", "mensagem": "Dados salvos/atualizados com sucesso!"})

    except Exception as e:
        return jsonify({"erro": str(e)}), 500


@app.route('/consultar', methods=['GET'])
def consultar_pesquisa():
    """
    Consulta 1 contato específico: /consultar?contato=...
    """
    contato = request.args.get("contato")

    if not contato:
        return jsonify({"erro": "Parâmetro 'contato' é obrigatório na query string"}), 400

    try:
        conn = conectar()
        cur = conn.cursor()

        colunas = ", ".join([f"questao{i}" for i in range(1, 59)])
        sql = f"""
            SELECT contato, {colunas}
            FROM public.whuana
            WHERE contato = %s;
        """

        cur.execute(sql, (contato,))
        row = cur.fetchone()
        cur.close()
        conn.close()

        if not row:
            return jsonify({"erro": "Contato não encontrado"}), 404

        resultado = {"contato": row[0]}
        for i in range(1, 59):
            resultado[f"questao{i}"] = row[i]

        return jsonify(resultado)

    except Exception as e:
        return jsonify({"erro": str(e)}), 500


@app.route('/consultar-todos', methods=['GET'])
def consultar_todos():
    """
    Consulta todas as inserções da tabela public.whuana
    """
    try:
        conn = conectar()
        cur = conn.cursor()

        colunas = ", ".join([f"questao{i}" for i in range(1, 59)])
        sql = f"""
            SELECT contato, {colunas}
            FROM public.whuana
            ORDER BY contato;
        """
        cur.execute(sql)
        rows = cur.fetchall()
        cur.close()
        conn.close()

        resultados = []
        for row in rows:
            item = {"contato": row[0]}
            for i in range(1, 59):
                item[f"questao{i}"] = row[i]
            resultados.append(item)

        return jsonify({
            "total": len(resultados),
            "resultados": resultados
        })

    except Exception as e:
        return jsonify({"erro": str(e)}), 500


@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "API rodando"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)
