from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def root():
    return {"message": "server is running"}

@app.post("/webhook")
async def github_webhook(request: Request):
    payload = await request.json()
    print(payload)
    return {"status": "ok"}