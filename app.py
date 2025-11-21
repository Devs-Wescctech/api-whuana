from flask import Flask, request, jsonify
import psycopg2

app = Flask(__name__)

def conectar():
    return psycopg2.connect(
        host="localhost",
        database="clientes_db",   # seu banco
        user="postgres",
        password="1234",          # sua senha
        port=5432
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
            INSERT INTO pesquisa (
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
                sexo = COALESCE(EXCLUDED.sexo, pesquisa.sexo),
                genero = COALESCE(EXCLUDED.genero, pesquisa.genero),
                idade = COALESCE(EXCLUDED.idade, pesquisa.idade),
                estadocivil = COALESCE(EXCLUDED.estadocivil, pesquisa.estadocivil),
                escolaridade = COALESCE(EXCLUDED.escolaridade, pesquisa.escolaridade),
                numerofilhos = COALESCE(EXCLUDED.numerofilhos, pesquisa.numerofilhos),
                planosaude = COALESCE(EXCLUDED.planosaude, pesquisa.planosaude),
                tempoempresa = COALESCE(EXCLUDED.tempoempresa, pesquisa.tempoempresa),
                atvdpromocaoempresa = COALESCE(EXCLUDED.atvdpromocaoempresa, pesquisa.atvdpromocaoempresa),
                motivoatvdpromocaoempresa = COALESCE(EXCLUDED.motivoatvdpromocaoempresa, pesquisa.motivoatvdpromocaoempresa),
                frequenciaatvdpromocaoempresa = COALESCE(EXCLUDED.frequenciaatvdpromocaoempresa, pesquisa.frequenciaatvdpromocaoempresa)
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


@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "API rodando"})


if __name__ == '__main__':
    app.run(debug=True, port=5001)