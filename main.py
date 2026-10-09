from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "API activa en Vercel", "framework": "FastAPI"}

@app.get("/predict")
def predict(x: float):
    result = x * 2
    return {"input": x, "prediction": result}