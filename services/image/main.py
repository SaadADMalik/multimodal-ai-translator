from fastapi import FastAPI

app = FastAPI(title="Image Service")

@app.get("/")
async def root():
    return {"message": "Image Service"}