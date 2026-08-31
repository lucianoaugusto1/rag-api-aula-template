# RAG API Aula - Template Inicial

Template inicial para os alunos implementarem uma API de busca RAG com FastAPI.

Este repositório vem com o ambiente configurado, dependências instaláveis via `uv`, arquivo `.http` com exemplos de chamadas, base `data/filmes.json`, app FastAPI mínimo e pastas base do projeto. Ele não inclui o código da solução das buscas.

## O que vem pronto

- `pyproject.toml` com as bibliotecas da aula.
- `uv.lock` gerado pelo `uv`.
- `.python-version` com Python 3.12.
- `.env.example` com os nomes das variáveis de ambiente.
- `.http` na raiz com exemplos de requests.
- `main.py` e `api/app.py` com FastAPI iniciado.
- `core/preprocessing.py` com carregamento inicial dos recursos do NLTK.
- `data/filmes.json` com a base de filmes da aula.
- Pastas `api/`, `core/`, `data/`, `images/` e `cache/`.

## Requisitos

- [Python 3.12 ou superior](https://www.python.org/downloads/)
- [`uv`](https://docs.astral.sh/uv/)
- [Git](https://git-scm.com/downloads)

Para instalar o `uv`:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Links úteis

- [FastAPI](https://fastapi.tiangolo.com/): framework para criar a API.
- [Uvicorn](https://www.uvicorn.org/): servidor usado para rodar o FastAPI.
- [Groq Console](https://console.groq.com/): local para gerar a chave `GROQ_API_KEY`.
- [Google AI Studio](https://aistudio.google.com/): local para gerar a chave `GOOGLE_API_KEY` do Gemini.
- [Google Gen AI SDK](https://ai.google.dev/gemini-api/docs): documentação do SDK do Gemini.
- [ChromaDB](https://docs.trychroma.com/): vector store para busca vetorial.
- [Sentence Transformers](https://www.sbert.net/): biblioteca para embeddings e busca semântica.
- [NLTK](https://www.nltk.org/): biblioteca para processamento de texto.

## Como configurar

Clone o projeto:

```bash
git clone https://github.com/lucianoaugusto1/rag-api-aula-template.git
cd rag-api-aula-template
```

Instale as dependências:

```bash
uv sync
```

Crie o arquivo `.env` a partir do exemplo:

```bash
cp .env.example .env
```

Preencha as chaves quando for usar rotas com LLM ou Gemini:

```env
GROQ_API_KEY=sua-chave-groq
GOOGLE_API_KEY=sua-chave-google
```

Não faça commit do arquivo `.env`.

## Como subir a API

O template já sobe com a rota `/health`:

```bash
uv run uvicorn api.app:app --reload
```

A API ficará disponível em:

```text
http://127.0.0.1:8000
```

A documentação interativa ficará em:

```text
http://127.0.0.1:8000/docs
```

Teste a rota inicial:

```bash
curl http://127.0.0.1:8000/health
```

Resposta esperada:

```json
{"status":"ok"}
```

## Como usar o arquivo `.http`

O arquivo `.http` na raiz contém exemplos de chamadas para as rotas esperadas da aula.

Você pode usar esse arquivo com extensões como:

- [REST Client para VS Code](https://marketplace.visualstudio.com/items?itemName=humao.rest-client)
- [HTTP Client da JetBrains](https://www.jetbrains.com/help/idea/http-client-in-product-code-editor.html)

A chamada `/health` já funciona. As outras chamadas vão funcionar depois que as rotas forem implementadas pelos alunos.

## Estrutura sugerida

```text
.
├── api/
│   ├── __init__.py
│   └── app.py
├── cache/
├── core/
│   ├── __init__.py
│   └── preprocessing.py
├── data/
│   └── filmes.json
├── images/
├── .env.example
├── .gitignore
├── .http
├── .python-version
├── main.py
├── pyproject.toml
├── README.md
└── uv.lock
```

## Dependências principais

- `fastapi`
- `uvicorn`
- `chromadb`
- `google-genai`
- `groq`
- `nltk`
- `numpy`
- `pillow`
- `python-multipart`
- `sentence-transformers`

## Observações para os alunos

- Implemente o código dentro de `api/` e `core/`.
- Use a base de filmes em `data/filmes.json`.
- Coloque imagens de teste em `images/`.
- Use `cache/` apenas para arquivos gerados localmente.
- Nunca suba chaves de API para o GitHub.
- Antes de commitar, revise:

```bash
git status
git diff
```
