# API WHUANA

API em Flask para inserção e atualização progressiva de dados de pesquisa no PostgreSQL.

## Endpoints

### `POST /inserir`
Insere ou atualiza dados progressivamente usando `ON CONFLICT (contato)`.

**Body (JSON):**
```json
{
  "contato": "555199999999",
  "sexo": "M",
  "genero": "Masculino",
  "idade": 30,
  "estadocivil": "Solteiro",
  "escolaridade": "Superior",
  "numerofilhos": 0,
  "planosaude": "Sim",
  "tempoempresa": "2 anos",
  "atvdpromocaoempresa": "Sim",
  "motivoatvdpromocaoempresa": "Benefícios",
  "frequenciaatvdpromocaoempresa": "Mensal"
}
```

### `GET /`
Retorna status da API.

## Docker / GHCR

A imagem é gerada automaticamente no GitHub Container Registry (GHCR) quando houver push na branch `main`.

Imagem esperada:
```
ghcr.io/devs-wescctech/api-whuana:latest
```

### Observação importante sobre PostgreSQL
No seu `app.py`, a conexão está configurada com `host="localhost"`.  
Dentro do container, `localhost` aponta para o próprio container.  
Para acessar o Postgres que está no host, ajuste para o IP do servidor (ex.: `172.16.x.x`) **ou** rode o container com `--network host`.

COMANDO PARA RECRIAR CONTAINER APOS ATUALIZAR O APP.PY
docker pull ghcr.io/devs-wescctech/api-whuana:latest

docker rm -f api-whuana

docker run -d \
  --name api-whuana \
  --restart always \
  -p 5020:5000 \
  ghcr.io/devs-wescctech/api-whuana:latest
