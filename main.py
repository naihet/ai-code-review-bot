from fastapi import FastAPI, Request

app = FastAPI()

# =========================
# Health check endpoint
# =========================
@app.get("/")
def root():
    # server check
    return {"message": "server is running"}


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
    print("Diff URL:", pr.get("diff_url"))

    print("======== END ========\n")

    return {"status": "ok"}