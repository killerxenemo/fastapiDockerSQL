from fastapi import FastAPI
import datetime
from database import DB
from pydantic import BaseModel

app = FastAPI()
db=DB()

class Configuracio(BaseModel):
    host: str
    port: int
    user: str
    password: str
    database: str

@app.get("/")
def read_root():
    if db.dbconfigurada:
        return {"message": "Benvingut, DB configurada"}
    else:
        return {"message": "Has de configurar la DB abans de continuar"}

@app.post("/configuraDB")
async def configuraDB(configuracio:Configuracio):
    db.configuraDB(configuracio)
    return True

@app.get("/vols")
def read_vols():
    db.conecta()
    resposta=db.cargaAeroports()
    db.desconecta()
    return resposta


