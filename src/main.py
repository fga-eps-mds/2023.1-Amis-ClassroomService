from dotenv import load_dotenv
load_dotenv()
#importa a rota aqui

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

# exemplo de rota
#app.include_router(login_router)


@app.get('/')
async def root():
    return {"message": "Amis !"}