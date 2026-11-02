from fastapi import FastAPI, APIRouter
import subprocess
from .vm import startvm, listvm

app = FastAPI()
router = APIRouter()

@app.post("/instances/{name}/{typ}/startvm")
def start(name, typ):
    startvm(name, typ)


@app.get('/instances/listvm')
def list():
    listvm()