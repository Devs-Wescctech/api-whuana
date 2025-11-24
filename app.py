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
    Converte valores inválidos em None:
    - None ou string vazia -> None
    - valor começando com "$contato." -> None
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
    questao1 = limpar_valor(dados.get("questao1"))
    questao2 = limpar_valor(dados.get("questao2"))
    questao3 = limpar_valor(dados.get("questao3"))
    questao4 = limpar_valor(dados.get("questao4"))
    questao5 = limpar_valor(dados.get("questao5"))
    questao6 = limpar_valor(dados.get("questao6"))
    questao7 = limpar_valor(dados.get("questao7"))
    questao8 = limpar_valor(dados.get("questao8"))
    questao9 = limpar_valor(dados.get("questao9"))
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

    try:
        conn = conectar()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO public.whuana AS whuana (
                contato,
                questao1,
                questao2,
                questao3,
                questao4,
                questao5,
                questao6,
                questao7,
                questao8,
                questao9,
                questao10,
                questao11,
                questao12,
                questao13,
                questao14,
                questao15,
                questao16,
                questao17,
                questao18,
                questao19,
                questao20,
                questao21,
                questao22,
                questao23,
                questao24,
                questao25,
                questao26,
                questao27,
                questao28,
                questao29,
                questao30,
                questao31,
                questao32,
                questao33,
                questao34,
                questao35,
                questao36,
                questao37,
                questao38,
                questao39,
                questao40,
                questao41,
                questao42,
                questao43,
                questao44,
                questao45,
                questao46,
                questao47,
                questao48,
                questao49,
                questao50,
                questao51,
                questao52,
                questao53,
                questao54,
                questao55,
                questao56,
                questao57,
                questao58
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (contato) DO UPDATE SET
                questao1 = COALESCE(EXCLUDED.questao1, whuana.questao1),
                questao2 = COALESCE(EXCLUDED.questao2, whuana.questao2),
                questao3 = COALESCE(EXCLUDED.questao3, whuana.questao3),
                questao4 = COALESCE(EXCLUDED.questao4, whuana.questao4),
                questao5 = COALESCE(EXCLUDED.questao5, whuana.questao5),
                questao6 = COALESCE(EXCLUDED.questao6, whuana.questao6),
                questao7 = COALESCE(EXCLUDED.questao7, whuana.questao7),
                questao8 = COALESCE(EXCLUDED.questao8, whuana.questao8),
                questao9 = COALESCE(EXCLUDED.questao9, whuana.questao9),
                questao10 = COALESCE(EXCLUDED.questao10, whuana.questao10),
                questao11 = COALESCE(EXCLUDED.questao11, whuana.questao11),
                questao12 = COALESCE(EXCLUDED.questao12, whuana.questao12),
                questao13 = COALESCE(EXCLUDED.questao13, whuana.questao13),
                questao14 = COALESCE(EXCLUDED.questao14, whuana.questao14),
                questao15 = COALESCE(EXCLUDED.questao15, whuana.questao15),
                questao16 = COALESCE(EXCLUDED.questao16, whuana.questao16),
                questao17 = COALESCE(EXCLUDED.questao17, whuana.questao17),
                questao18 = COALESCE(EXCLUDED.questao18, whuana.questao18),
                questao19 = COALESCE(EXCLUDED.questao19, whuana.questao19),
                questao20 = COALESCE(EXCLUDED.questao20, whuana.questao20),
                questao21 = COALESCE(EXCLUDED.questao21, whuana.questao21),
                questao22 = COALESCE(EXCLUDED.questao22, whuana.questao22),
                questao23 = COALESCE(EXCLUDED.questao23, whuana.questao23),
                questao24 = COALESCE(EXCLUDED.questao24, whuana.questao24),
                questao25 = COALESCE(EXCLUDED.questao25, whuana.questao25),
                questao26 = COALESCE(EXCLUDED.questao26, whuana.questao26),
                questao27 = COALESCE(EXCLUDED.questao27, whuana.questao27),
                questao28 = COALESCE(EXCLUDED.questao28, whuana.questao28),
                questao29 = COALESCE(EXCLUDED.questao29, whuana.questao29),
                questao30 = COALESCE(EXCLUDED.questao30, whuana.questao30),
                questao31 = COALESCE(EXCLUDED.questao31, whuana.questao31),
                questao32 = COALESCE(EXCLUDED.questao32, whuana.questao32),
                questao33 = COALESCE(EXCLUDED.questao33, whuana.questao33),
                questao34 = COALESCE(EXCLUDED.questao34, whuana.questao34),
                questao35 = COALESCE(EXCLUDED.questao35, whuana.questao35),
                questao36 = COALESCE(EXCLUDED.questao36, whuana.questao36),
                questao37 = COALESCE(EXCLUDED.questao37, whuana.questao37),
                questao38 = COALESCE(EXCLUDED.questao38, whuana.questao38),
                questao39 = COALESCE(EXCLUDED.questao39, whuana.questao39),
                questao40 = COALESCE(EXCLUDED.questao40, whuana.questao40),
                questao41 = COALESCE(EXCLUDED.questao41, whuana.questao41),
                questao42 = COALESCE(EXCLUDED.questao42, whuana.questao42),
                questao43 = COALESCE(EXCLUDED.questao43, whuana.questao43),
                questao44 = COALESCE(EXCLUDED.questao44, whuana.questao44),
                questao45 = COALESCE(EXCLUDED.questao45, whuana.questao45),
                questao46 = COALESCE(EXCLUDED.questao46, whuana.questao46),
                questao47 = COALESCE(EXCLUDED.questao47, whuana.questao47),
                questao48 = COALESCE(EXCLUDED.questao48, whuana.questao48),
                questao49 = COALESCE(EXCLUDED.questao49, whuana.questao49),
                questao50 = COALESCE(EXCLUDED.questao50, whuana.questao50),
                questao51 = COALESCE(EXCLUDED.questao51, whuana.questao51),
                questao52 = COALESCE(EXCLUDED.questao52, whuana.questao52),
                questao53 = COALESCE(EXCLUDED.questao53, whuana.questao53),
                questao54 = COALESCE(EXCLUDED.questao54, whuana.questao54),
                questao55 = COALESCE(EXCLUDED.questao55, whuana.questao55),
                questao56 = COALESCE(EXCLUDED.questao56, whuana.questao56),
                questao57 = COALESCE(EXCLUDED.questao57, whuana.questao57),
                questao58 = COALESCE(EXCLUDED.questao58, whuana.questao58)
        """, (
            contato,
            questao1,
            questao2,
            questao3,
            questao4,
            questao5,
            questao6,
            questao7,
            questao8,
            questao9,
            questao10,
            questao11,
            questao12,
            questao13,
            questao14,
            questao15,
            questao16,
            questao17,
            questao18,
            questao19,
            questao20,
            questao21,
            questao22,
            questao23,
            questao24,
            questao25,
            questao26,
            questao27,
            questao28,
            questao29,
            questao30,
            questao31,
            questao32,
            questao33,
            questao34,
            questao35,
            questao36,
            questao37,
            questao38,
            questao39,
            questao40,
            questao41,
            questao42,
            questao43,
            questao44,
            questao45,
            questao46,
            questao47,
            questao48,
            questao49,
            questao50,
            questao51,
            questao52,
            questao53,
            questao54,
            questao55,
            questao56,
            questao57,
            questao58
        ))

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

        cur.execute("""
            SELECT
                contato,
                questao1,
                questao2,
                questao3,
                questao4,
                questao5,
                questao6,
                questao7,
                questao8,
                questao9,
                questao10,
                questao11,
                questao12,
                questao13,
                questao14,
                questao15,
                questao16,
                questao17,
                questao18,
                questao19,
                questao20,
                questao21,
                questao22,
                questao23,
                questao24,
                questao25,
                questao26,
                questao27,
                questao28,
                questao29,
                questao30,
                questao31,
                questao32,
                questao33,
                questao34,
                questao35,
                questao36,
                questao37,
                questao38,
                questao39,
                questao40,
                questao41,
                questao42,
                questao43,
                questao44,
                questao45,
                questao46,
                questao47,
                questao48,
                questao49,
                questao50,
                questao51,
                questao52,
                questao53,
                questao54,
                questao55,
                questao56,
                questao57,
                questao58
            FROM public.whuana
            WHERE contato = %s
        """, (contato,))

        row = cur.fetchone()
        cur.close()
        conn.close()

        if not row:
            return jsonify({"erro": "Contato não encontrado"}), 404

        resultado = {
            "contato": row[0],
            "questao1": row[1],
            "questao2": row[2],
            "questao3": row[3],
            "questao4": row[4],
            "questao5": row[5],
            "questao6": row[6],
            "questao7": row[7],
            "questao8": row[8],
            "questao9": row[9],
            "questao10": row[10],
            "questao11": row[11],
            "questao12": row[12],
            "questao13": row[13],
            "questao14": row[14],
            "questao15": row[15],
            "questao16": row[16],
            "questao17": row[17],
            "questao18": row[18],
            "questao19": row[19],
            "questao20": row[20],
            "questao21": row[21],
            "questao22": row[22],
            "questao23": row[23],
            "questao24": row[24],
            "questao25": row[25],
            "questao26": row[26],
            "questao27": row[27],
            "questao28": row[28],
            "questao29": row[29],
            "questao30": row[30],
            "questao31": row[31],
            "questao32": row[32],
            "questao33": row[33],
            "questao34": row[34],
            "questao35": row[35],
            "questao36": row[36],
            "questao37": row[37],
            "questao38": row[38],
            "questao39": row[39],
            "questao40": row[40],
            "questao41": row[41],
            "questao42": row[42],
            "questao43": row[43],
            "questao44": row[44],
            "questao45": row[45],
            "questao46": row[46],
            "questao47": row[47],
            "questao48": row[48],
            "questao49": row[49],
            "questao50": row[50],
            "questao51": row[51],
            "questao52": row[52],
            "questao53": row[53],
            "questao54": row[54],
            "questao55": row[55],
            "questao56": row[56],
            "questao57": row[57],
            "questao58": row[58],
        }

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

        cur.execute("""
            SELECT
                contato,
                questao1,
                questao2,
                questao3,
                questao4,
                questao5,
                questao6,
                questao7,
                questao8,
                questao9,
                questao10,
                questao11,
                questao12,
                questao13,
                questao14,
                questao15,
                questao16,
                questao17,
                questao18,
                questao19,
                questao20,
                questao21,
                questao22,
                questao23,
                questao24,
                questao25,
                questao26,
                questao27,
                questao28,
                questao29,
                questao30,
                questao31,
                questao32,
                questao33,
                questao34,
                questao35,
                questao36,
                questao37,
                questao38,
                questao39,
                questao40,
                questao41,
                questao42,
                questao43,
                questao44,
                questao45,
                questao46,
                questao47,
                questao48,
                questao49,
                questao50,
                questao51,
                questao52,
                questao53,
                questao54,
                questao55,
                questao56,
                questao57,
                questao58
            FROM public.whuana
            ORDER BY contato
        """)

        rows = cur.fetchall()
        cur.close()
        conn.close()

        resultados = []
        for row in rows:
            resultados.append({
                "contato": row[0],
                "questao1": row[1],
                "questao2": row[2],
                "questao3": row[3],
                "questao4": row[4],
                "questao5": row[5],
                "questao6": row[6],
                "questao7": row[7],
                "questao8": row[8],
                "questao9": row[9],
                "questao10": row[10],
                "questao11": row[11],
                "questao12": row[12],
                "questao13": row[13],
                "questao14": row[14],
                "questao15": row[15],
                "questao16": row[16],
                "questao17": row[17],
                "questao18": row[18],
                "questao19": row[19],
                "questao20": row[20],
                "questao21": row[21],
                "questao22": row[22],
                "questao23": row[23],
                "questao24": row[24],
                "questao25": row[25],
                "questao26": row[26],
                "questao27": row[27],
                "questao28": row[28],
                "questao29": row[29],
                "questao30": row[30],
                "questao31": row[31],
                "questao32": row[32],
                "questao33": row[33],
                "questao34": row[34],
                "questao35": row[35],
                "questao36": row[36],
                "questao37": row[37],
                "questao38": row[38],
                "questao39": row[39],
                "questao40": row[40],
                "questao41": row[41],
                "questao42": row[42],
                "questao43": row[43],
                "questao44": row[44],
                "questao45": row[45],
                "questao46": row[46],
                "questao47": row[47],
                "questao48": row[48],
                "questao49": row[49],
                "questao50": row[50],
                "questao51": row[51],
                "questao52": row[52],
                "questao53": row[53],
                "questao54": row[54],
                "questao55": row[55],
                "questao56": row[56],
                "questao57": row[57],
                "questao58": row[58],
            })

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
