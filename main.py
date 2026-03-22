from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
from ai import recomendar_com_ia
from auth import gerar_token

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/racas")
def racas():
    return requests.get("https://api.thedogapi.com/v1/breeds").json()

@app.post("/login")
def login():
    return {"token": gerar_token(1)}

@app.post("/recomendar")
def recomendar(dados: dict):
    racas = requests.get("https://api.thedogapi.com/v1/breeds").json()
    resposta = recomendar_com_ia(dados, racas[:20])
    return {"resultado": resposta}
