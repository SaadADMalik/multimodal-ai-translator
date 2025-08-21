from fastapi import FastAPI

app = FastAPI(title="Translation Service")

@app.get("/")
async def root():
    return {"message": "Translation Service"}