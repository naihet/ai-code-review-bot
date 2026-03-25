from fastapi import FastAPI, Request
from reviewer import process_pr
import requests

app = FastAPI()

# =========================
# Health check endpoint
# =========================
@app.get("/")
def root():
    # server check
    return {"message": "server is running"}

def get_diff(diff_url):
    headers = {
        "Accept": "application/vnd.github.v3.diff"
    }
    response = requests.get(diff_url, headers=headers)

    if response.status_code != 200:
        print("Failed to fetch diff:", response.status_code)
        return None

    return response.text

# =========================
# GitHub Webhook endpoint
# =========================
@app.post("/webhook")
async def github_webhook(request: Request):
    payload = await request.json()

    print("\n======== WEBHOOK HIT ========")
    print("PAYLOAD KEYS:", payload.keys())
    print("ACTION:", payload.get("action"))

    if "pull_request" in payload:
        print("✅ HAS PR")
    else:
        print("❌ NO PR")

    if "pull_request" not in payload:
        return {"status": "ignored"}

    pr = payload["pull_request"]

    # reviewer
    review = process_pr(pr)

    return {"status": "ok"}