from fastapi import FastAPI

app = FastAPI(title="STT Service")

@app.get("/")
async def root():
    return {"message": "STT Service"}