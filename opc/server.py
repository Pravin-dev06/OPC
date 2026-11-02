from fastapi import FastAPI, APIRouter
import subprocess

app = FastAPI()
router = APIRouter()

@app.post("/instances/{name}/{typ}/startvm")
def startvm(name, typ):
    cmd = f'VBoxManage startvm "{name}" --type={typ}'
    subprocess.run(cmd.split())