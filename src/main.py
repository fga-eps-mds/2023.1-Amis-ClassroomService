from dotenv import load_dotenv
load_dotenv()
#importa a rota aqui

from src.application.controllers.CursoController import router_curso as curso_router
from src.application.controllers.InstrucaoCapacitacaoController import router_instrucao 
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

load_dotenv()
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(curso_router)
app.include_router(router_instrucao)


@app.get('/')
async def root():
    return {"message": "Amis !"}