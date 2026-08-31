# Security

Este projeto é um template de aula, mas deve seguir cuidados básicos de segurança desde o início.

## Segredos

Nunca faça commit de chaves, tokens ou arquivos `.env`.

Use variáveis de ambiente:

```env
GROQ_API_KEY=
GOOGLE_API_KEY=
```

Se uma chave aparecer em commit, push bloqueado, print, aula gravada ou chat, considere a chave comprometida e revogue imediatamente no provedor.

## Cache local

Arquivos em `cache/` são gerados localmente e não devem ser versionados.

Se os alunos implementarem cache com `pickle`, carregue arquivos `.pkl` apenas quando eles foram gerados localmente. Nunca aceite ou carregue arquivos `.pkl` enviados por terceiros.

## Deploy público

Antes de expor a API na internet:

- Adicione autenticação.
- Adicione rate limit.
- Proteja rotas que chamam Groq ou Gemini, pois elas podem gerar custo.
- Configure CORS de forma restrita.
- Não exponha `.env`, cache, `.venv` ou arquivos internos.

## Dependências

Rode auditoria periodicamente:

```bash
make audit
```

Observação: no momento da criação deste material, `pip-audit` aponta vulnerabilidades conhecidas em `chromadb==1.5.9` sem listar versão corrigida. Antes de usar este template fora da aula/local, confira se já existe uma versão corrigida de `chromadb` e atualize o lockfile.
