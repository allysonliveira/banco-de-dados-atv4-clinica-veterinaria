from fastapi import FastAPI
from api import clinica_api, veterinario_api, tutor_api, pet_api, atendimento_api

app = FastAPI(
    title="API de Gerenciamento de Clínicas Veterinárias",
    version="1.0"
)

# Incluindo rotas
app.include_router(clinica_api.router)
app.include_router(veterinario_api.router)
app.include_router(tutor_api.router)
app.include_router(pet_api.router)
app.include_router(atendimento_api.router)