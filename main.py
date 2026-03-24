from fastapi import FastAPI, Request
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
    # get payload from GitHub (JSON)
    payload = await request.json()

    print("\n======== WEBHOOK HIT ========")

    # show event type such
    action = payload.get("action")
    print("ACTION:", action)

    # Prevent error if not PR event
    if "pull_request" not in payload:
        print("Not a pull request event")
        return {"status": "ignored"}

    # get PR
    pr = payload["pull_request"]

    # info
    print("PR Title:", pr.get("title"))
    print("PR URL:", pr.get("html_url"))
    print("Repo:", payload["repository"]["full_name"])

    # get diff URL
    diff_url = pr.get("diff_url")
    print("Diff URL:", diff_url)
    diff = get_diff(diff_url)

    if diff:
        print("===== DIFF START =====")
        print(diff[:1000])  # ตัดแค่ 1000 ตัวอักษร (กันยาวเกิน)
        print("===== DIFF END =====")

    return {"status": "ok"}