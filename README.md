# Sistema de Gerenciamento de Clínicas Veterinárias

Este projeto é uma API RESTful desenvolvida com FastAPI, SQLAlchemy e PostgreSQL para gerenciar clínicas veterinárias, seus profissionais, tutores, pets e atendimentos.
O sistema segue as instruções propostas na Atividade 04 da disciplina DCA3604 - BANCO DE DADOS.

## Intruções do trabalho

1. Modelagem ORM
- Implemente as classes em SQLAlchemy com os campos e tipos apropriados.
- Use relationship e ForeignKey para expressar os relacionamentos entre as
entidades.
- Permita acesso aos objetos relacionados por meio de atributos Python (por
exemplo: atendimento.pet.nome ou clinica.veterinarios).

2. Organização do Projeto
Estruture o projeto em camadas, como a seguir:
/veterinaria
├── models/ # ORM: classes de mapeamento
├── repositories/ # Operações diretas com o banco
├── services/ # Lógica de negócio
├── api/ # Endpoints (rotas REST)
├── database.py # Engine e sessão do SQLAlchemy
├── main.py # Inicialização do app
└── requirements.txt # Dependências 

3. API REST
Implemente um conjunto de endpoints para as operações básicas:

Clínicas:
- POST /clinicas: cadastrar nova clínica
-  GET /clinicas: listar clínicas
-  GET /clinicas/{id}: listar clínica específica
-  GET /clinicas/{id}/veterinarios: listar veterinários de uma clínica

Veterinários:
- POST /veterinarios
- GET /veterinarios

Tutores:
- POST /tutores
- GET /tutores/{id}/pets

Pets:
- POST /pets
- GET /pets
- GET /pets/{id}/atendimentos

Atendimentos:
- POST /atendimentos: criar um novo atendimento
- GET /atendimentos
- GET /veterinarios/{id}/atendimentos

(Crie outros endpoints caso identifique a necessidade)

## Tecnologias obrigatórias
- Banco de dados PostgreSQL
- ORM SQLAlchemy (de preferência com declarative base)
- Backend com FastAPI (ou Flask)
- Comunicação via JSON
- Uso de Pydantic para validação de entrada (se usar FastAPI)
- Documentação automática com Swagger (FastAPI) 

### Como executar o sistema criado deste repositório

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

## 🧪 Abrir no GitHub Codespaces

Você pode editar e rodar este projeto diretamente no navegador com o GitHub Codespaces (requer login):

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?repo=SEU_REPOSITORIO&quickstart=1)
