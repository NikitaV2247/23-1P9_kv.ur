"""FastAPI к квадратному уравнению"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from logic import kv_ur

app = FastAPI()

app.mount("/static", StaticFiles(directory="public"))


@app.get("/kv_ur")
def kv_ur_get(a, b, c):
    """эндпоинт для нахождения корней квадратного уравнения"""
    a = float(a)
    b = float(b)
    c = float(c)
    return kv_ur(a, b, c)
