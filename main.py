from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "API activa en Vercel", "framework": "FastAPI"}

@app.get("/predict")
def predict(x: float):
    result = x * 2
    return {"input": x, "prediction": result}

@app.get("/nuevo/{numero}")
def dividir(numero: float):
    result = numero // 2
    return {"el resultado es ": result}
