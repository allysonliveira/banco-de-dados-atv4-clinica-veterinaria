# Sistema de Gerenciamento de Clínicas Veterinárias

Este projeto é uma API RESTful desenvolvida com FastAPI, SQLAlchemy e PostgreSQL para gerenciar clínicas veterinárias, seus profissionais, tutores, pets e atendimentos.

## Como executar

1. Crie o banco de dados PostgreSQL:
   - Nome: `veterinaria_db`
   - Usuário e senha devem ser ajustados em `database.py`

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Rode o servidor:
```bash
uvicorn main:app --reload
```

## Documentação

Acesse a documentação automática gerada pelo Swagger:

[http://localhost:8000/docs](http://localhost:8000/docs)

## Estrutura

- `models/`: tabelas SQLAlchemy
- `schemas/`: validações Pydantic
- `repositories/`: acesso ao banco
- `services/`: lógica de negócio
- `api/`: rotas FastAPI