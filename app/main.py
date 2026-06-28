from fastapi import FastAPI

app = FastAPI(title="pramana")

@app.get("/health")
def health():
    return {"status":"masta"}


