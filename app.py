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

def limpar_valor(v):
    """
    - None -> None
    - string vazia -> None
    - começa com "$contato." -> None
    - resto mantém
    """
    if v is None:
        return None
    if isinstance(v, str):
        v2 = v.strip()
        if v2 == "":
            return None
        if v2.startswith("$contato."):
            return None
        return v2
    return v


@app.route('/inserir', methods=['POST'])
def inserir_ou_atualizar_pesquisa():
    dados = request.get_json() or {}

    contato = dados.get("contato")

    # questoes 01..09 com zero à esquerda
    questao01 = limpar_valor(dados.get("questao01"))
    questao02 = limpar_valor(dados.get("questao02"))
    questao03 = limpar_valor(dados.get("questao03"))
    questao04 = limpar_valor(dados.get("questao04"))
    questao05 = limpar_valor(dados.get("questao05"))
    questao06 = limpar_valor(dados.get("questao06"))
    questao07 = limpar_valor(dados.get("questao07"))
    questao08 = limpar_valor(dados.get("questao08"))
    questao09 = limpar_valor(dados.get("questao09"))
    # questoes 10..58 normais
    questao10 = limpar_valor(dados.get("questao10"))
    questao11 = limpar_valor(dados.get("questao11"))
    questao12 = limpar_valor(dados.get("questao12"))
    questao13 = limpar_valor(dados.get("questao13"))
    questao14 = limpar_valor(dados.get("questao14"))
    questao15 = limpar_valor(dados.get("questao15"))
    questao16 = limpar_valor(dados.get("questao16"))
    questao17 = limpar_valor(dados.get("questao17"))
    questao18 = limpar_valor(dados.get("questao18"))
    questao19 = limpar_valor(dados.get("questao19"))
    questao20 = limpar_valor(dados.get("questao20"))
    questao21 = limpar_valor(dados.get("questao21"))
    questao22 = limpar_valor(dados.get("questao22"))
    questao23 = limpar_valor(dados.get("questao23"))
    questao24 = limpar_valor(dados.get("questao24"))
    questao25 = limpar_valor(dados.get("questao25"))
    questao26 = limpar_valor(dados.get("questao26"))
    questao27 = limpar_valor(dados.get("questao27"))
    questao28 = limpar_valor(dados.get("questao28"))
    questao29 = limpar_valor(dados.get("questao29"))
    questao30 = limpar_valor(dados.get("questao30"))
    questao31 = limpar_valor(dados.get("questao31"))
    questao32 = limpar_valor(dados.get("questao32"))
    questao33 = limpar_valor(dados.get("questao33"))
    questao34 = limpar_valor(dados.get("questao34"))
    questao35 = limpar_valor(dados.get("questao35"))
    questao36 = limpar_valor(dados.get("questao36"))
    questao37 = limpar_valor(dados.get("questao37"))
    questao38 = limpar_valor(dados.get("questao38"))
    questao39 = limpar_valor(dados.get("questao39"))
    questao40 = limpar_valor(dados.get("questao40"))
    questao41 = limpar_valor(dados.get("questao41"))
    questao42 = limpar_valor(dados.get("questao42"))
    questao43 = limpar_valor(dados.get("questao43"))
    questao44 = limpar_valor(dados.get("questao44"))
    questao45 = limpar_valor(dados.get("questao45"))
    questao46 = limpar_valor(dados.get("questao46"))
    questao47 = limpar_valor(dados.get("questao47"))
    questao48 = limpar_valor(dados.get("questao48"))
    questao49 = limpar_valor(dados.get("questao49"))
    questao50 = limpar_valor(dados.get("questao50"))
    questao51 = limpar_valor(dados.get("questao51"))
    questao52 = limpar_valor(dados.get("questao52"))
    questao53 = limpar_valor(dados.get("questao53"))
    questao54 = limpar_valor(dados.get("questao54"))
    questao55 = limpar_valor(dados.get("questao55"))
    questao56 = limpar_valor(dados.get("questao56"))
    questao57 = limpar_valor(dados.get("questao57"))
    questao58 = limpar_valor(dados.get("questao58"))

    if not contato:
        return jsonify({"erro": "Campo 'contato' é obrigatório"}), 400

    # ordem tem que bater com a lista de colunas
    questoes = [
        questao01, questao02, questao03, questao04, questao05,
        questao06, questao07, questao08, questao09,
        questao10, questao11, questao12, questao13, questao14,
        questao15, questao16, questao17, questao18, questao19,
        questao20, questao21, questao22, questao23, questao24,
        questao25, questao26, questao27, questao28, questao29,
        questao30, questao31, questao32, questao33, questao34,
        questao35, questao36, questao37, questao38, questao39,
        questao40, questao41, questao42, questao43, questao44,
        questao45, questao46, questao47, questao48, questao49,
        questao50, questao51, questao52, questao53, questao54,
        questao55, questao56, questao57, questao58
    ]

    # nomes das colunas na tabela
    colunas_01_09 = [f"questao0{i}" for i in range(1, 10)]  # questao01..questao09
    colunas_10_58 = [f"questao{i}" for i in range(10, 59)]  # questao10..questao58
    colunas = colunas_01_09 + colunas_10_58  # total 58

    try:
        conn = conectar()
        cur = conn.cursor()

        colunas_sql = ", ".join(colunas)
        placeholders = ", ".join(["%s"] * len(colunas))
        updates = ", ".join([
            f"{col} = COALESCE(EXCLUDED.{col}, whuana.{col})"
            for col in colunas
        ])

        sql = f"""
            INSERT INTO public.whuana AS whuana (
                contato,
                {colunas_sql}
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

        colunas_01_09 = [f"questao0{i}" for i in range(1, 10)]
        colunas_10_58 = [f"questao{i}" for i in range(10, 59)]
        colunas = colunas_01_09 + colunas_10_58
        colunas_sql = ", ".join(colunas)

        cur.execute(f"""
            SELECT
                contato,
                {colunas_sql}
            FROM public.whuana
            WHERE contato = %s
        """, (contato,))

        row = cur.fetchone()
        cur.close()
        conn.close()

        if not row:
            return jsonify({"erro": "Contato não encontrado"}), 404

        resultado = {"contato": row[0]}
        for idx, col in enumerate(colunas, start=1):
            resultado[col] = row[idx]

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

        colunas_01_09 = [f"questao0{i}" for i in range(1, 10)]
        colunas_10_58 = [f"questao{i}" for i in range(10, 59)]
        colunas = colunas_01_09 + colunas_10_58
        colunas_sql = ", ".join(colunas)

        cur.execute(f"""
            SELECT
                contato,
                {colunas_sql}
            FROM public.whuana
            ORDER BY contato
        """)

        rows = cur.fetchall()
        cur.close()
        conn.close()

        resultados = []
        for row in rows:
            item = {"contato": row[0]}
            for idx, col in enumerate(colunas, start=1):
                item[col] = row[idx]
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
