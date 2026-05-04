import requests
import os

def get_diff(diff_url):
    headers = {
        # tell GitHub need diff format
        "Accept": "application/vnd.github.v3.diff"
    }

    response = requests.get(diff_url, headers=headers)

    # Prevent error
    if response.status_code != 200:
        print("Failed to fetch diff:", response.status_code)
        return None

    return response.text

#def comment_pr(repo_full_name, pr_number, comment):
    token = os.getenv("GITHUB_TOKEN")

    if not token:
        print("Missing GITHUB_TOKEN")
        return

    url = f"https://api.github.com/repos/{repo_full_name}/issues/{pr_number}/comments"

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json"
    }

    data = {
        "body": f"## 🤖 AI Review\n\n{comment}"
    }

    response = requests.post(url, headers=headers, json=data)

    print("Comment status:", response.status_code)

    if response.status_code == 201:
        print("Comment posted!")
    else:
        print("Comment failed:", response.text)#