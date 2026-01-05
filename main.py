from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{"message":"Backend is working"}
@app.get("/health")
def health():
    return{"status":"ok"}
@app.get("/add")
def add(a: int, b: int):
    return{
        "a": a,
        "b": b,
        "sum":a + b
    }