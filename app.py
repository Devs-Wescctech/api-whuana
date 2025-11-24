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
    questao1 = dados.get("questao1")
    questao2 = dados.get("questao2")
    questao3 = dados.get("questao3")
    questao4 = dados.get("questao4")
    questao5 = dados.get("questao5")
    questao6 = dados.get("questao6")
    questao7 = dados.get("questao7")
    questao8 = dados.get("questao8")
    questao9 = dados.get("questao9")
    questao10 = dados.get("questao10")
    questao11 = dados.get("questao11")
    questao12 = dados.get("questao12")
    questao13 = dados.get("questao13")
    questao14 = dados.get("questao14")
    questao15 = dados.get("questao15")
    questao16 = dados.get("questao16")
    questao17 = dados.get("questao17")
    questao18 = dados.get("questao18")
    questao19 = dados.get("questao19")
    questao20 = dados.get("questao20")
    questao21 = dados.get("questao21")
    questao22 = dados.get("questao22")
    questao23 = dados.get("questao23")
    questao24 = dados.get("questao24")
    questao25 = dados.get("questao25")
    questao26 = dados.get("questao26")
    questao27 = dados.get("questao27")
    questao28 = dados.get("questao28")
    questao29 = dados.get("questao29")
    questao30 = dados.get("questao30")
    questao31 = dados.get("questao31")
    questao32 = dados.get("questao32")
    questao33 = dados.get("questao33")
    questao34 = dados.get("questao34")
    questao35 = dados.get("questao35")
    questao36 = dados.get("questao36")
    questao37 = dados.get("questao37")
    questao38 = dados.get("questao38")
    questao39 = dados.get("questao39")
    questao40 = dados.get("questao40")
    questao41 = dados.get("questao41")
    questao42 = dados.get("questao42")
    questao43 = dados.get("questao43")
    questao44 = dados.get("questao44")
    questao45 = dados.get("questao45")
    questao46 = dados.get("questao46")
    questao47 = dados.get("questao47")
    questao48 = dados.get("questao48")
    questao49 = dados.get("questao49")
    questao50 = dados.get("questao50")
    questao51 = dados.get("questao51")
    questao52 = dados.get("questao52")
    questao53 = dados.get("questao53")
    questao54 = dados.get("questao54")
    questao55 = dados.get("questao55")
    questao56 = dados.get("questao56")
    questao57 = dados.get("questao57")
    questao58 = dados.get("questao58")

    if not contato:
        return jsonify({"erro": "Campo 'contato' é obrigatório"}), 400

    # lista para ficar fácil passar no execute
    questoes = [
        questao1, questao2, questao3, questao4, questao5,
        questao6, questao7, questao8, questao9, questao10,
        questao11, questao12, questao13, questao14, questao15,
        questao16, questao17, questao18, questao19, questao20,
        questao21, questao22, questao23, questao24, questao25,
        questao26, questao27, questao28, questao29, questao30,
        questao31, questao32, questao33, questao34, questao35,
        questao36, questao37, questao38, questao39, questao40,
        questao41, questao42, questao43, questao44, questao45,
        questao46, questao47, questao48, questao49, questao50,
        questao51, questao52, questao53, questao54, questao55,
        questao56, questao57, questao58
    ]

    try:
        conn = conectar()
        cur = conn.cursor()

        # monta colunas, placeholders e updates de forma segura
        colunas = ", ".join([f"questao{i}" for i in range(1, 59)])
        placeholders = ", ".join(["%s"] * 58)
        updates = ", ".join([
            f"questao{i} = COALESCE(EXCLUDED.questao{i}, whuana.questao{i})"
            for i in range(1, 59)
        ])

        sql = f"""
            INSERT INTO public.whuana AS whuana (
                contato,
                {colunas}
            )
            VALUES (%s, {placeholders})
            ON CONFLICT (contato) DO UPDATE SET
                {updates}
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

        cur.execute(f"""
            SELECT
                contato,
                {colunas}
            FROM public.whuana
            WHERE contato = %s
        """, (contato,))

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

        cur.execute(f"""
            SELECT
                contato,
                {colunas}
            FROM public.whuana
            ORDER BY contato
        """)

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
