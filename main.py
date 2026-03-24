from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def root():
    return {"message": "server is running"}

@app.post("/webhook")
async def github_webhook(request: Request):
    payload = await request.json()

    print("WEBHOOK HIT!!!")
    print("ACTION:", payload.get("action"))

    print("FULL PAYLOAD:")
    print(payload)

    return {"status": "ok"}