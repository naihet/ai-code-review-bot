from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def root():
    return {"message": "server is running"}

@app.post("/webhook")
async def github_webhook(request: Request):
    payload = await request.json()

    print("ACTION:", payload.get("action"))
    
    if payload.get("action") in ["opened", "synchronize"]:
        pr = payload["pull_request"]

        print("PR Title:", pr["title"])
        print("PR URL:", pr["html_url"])
        print("Repo:", payload["repository"]["full_name"])
        
    return {"status": "ok"}