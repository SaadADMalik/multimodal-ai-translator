from fastapi import FastAPI

app = FastAPI(title="TTS Service")

@app.get("/")
async def root():
    return {"message": "TTS Service"}