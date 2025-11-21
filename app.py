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
    sexo = dados.get("sexo")
    genero = dados.get("genero")
    idade = dados.get("idade")
    estadocivil = dados.get("estadocivil")
    escolaridade = dados.get("escolaridade")
    numerofilhos = dados.get("numerofilhos")
    planosaude = dados.get("planosaude")
    tempoempresa = dados.get("tempoempresa")
    atvdpromocaoempresa = dados.get("atvdpromocaoempresa")
    motivoatvdpromocaoempresa = dados.get("motivoatvdpromocaoempresa")
    frequenciaatvdpromocaoempresa = dados.get("frequenciaatvdpromocaoempresa")

    if not contato:
        return jsonify({"erro": "Campo 'contato' é obrigatório"}), 400

    try:
        conn = conectar()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO public.whuana AS whuana (
                contato,
                sexo,
                genero,
                idade,
                estadocivil,
                escolaridade,
                numerofilhos,
                planosaude,
                tempoempresa,
                atvdpromocaoempresa,
                motivoatvdpromocaoempresa,
                frequenciaatvdpromocaoempresa
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (contato) DO UPDATE SET
                sexo = COALESCE(EXCLUDED.sexo, whuana.sexo),
                genero = COALESCE(EXCLUDED.genero, whuana.genero),
                idade = COALESCE(EXCLUDED.idade, whuana.idade),
                estadocivil = COALESCE(EXCLUDED.estadocivil, whuana.estadocivil),
                escolaridade = COALESCE(EXCLUDED.escolaridade, whuana.escolaridade),
                numerofilhos = COALESCE(EXCLUDED.numerofilhos, whuana.numerofilhos),
                planosaude = COALESCE(EXCLUDED.planosaude, whuana.planosaude),
                tempoempresa = COALESCE(EXCLUDED.tempoempresa, whuana.tempoempresa),
                atvdpromocaoempresa = COALESCE(EXCLUDED.atvdpromocaoempresa, whuana.atvdpromocaoempresa),
                motivoatvdpromocaoempresa = COALESCE(EXCLUDED.motivoatvdpromocaoempresa, whuana.motivoatvdpromocaoempresa),
                frequenciaatvdpromocaoempresa = COALESCE(EXCLUDED.frequenciaatvdpromocaoempresa, whuana.frequenciaatvdpromocaoempresa)
        """, (
            contato,
            sexo,
            genero,
            idade,
            estadocivil,
            escolaridade,
            numerofilhos,
            planosaude,
            tempoempresa,
            atvdpromocaoempresa,
            motivoatvdpromocaoempresa,
            frequenciaatvdpromocaoempresa
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
    Consulta os dados de um contato na tabela public.whuana
    Exemplo: GET /consultar?contato=51999999998
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
                sexo,
                genero,
                idade,
                estadocivil,
                escolaridade,
                numerofilhos,
                planosaude,
                tempoempresa,
                atvdpromocaoempresa,
                motivoatvdpromocaoempresa,
                frequenciaatvdpromocaoempresa
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
            "sexo": row[1],
            "genero": row[2],
            "idade": row[3],
            "estadocivil": row[4],
            "escolaridade": row[5],
            "numerofilhos": row[6],
            "planosaude": row[7],
            "tempoempresa": row[8],
            "atvdpromocaoempresa": row[9],
            "motivoatvdpromocaoempresa": row[10],
            "frequenciaatvdpromocaoempresa": row[11],
        }

        return jsonify(resultado)

    except Exception as e:
        return jsonify({"erro": str(e)}), 500


@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "API rodando"})


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=5000)
