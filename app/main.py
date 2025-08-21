from fastapi import FastAPI, WebSocket

app = FastAPI(title="Multimodal AI Translator")

@app.get("/")
async def root():
    return {"message": "Multimodal AI Translator API"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Received: {data}")