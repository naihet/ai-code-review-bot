import requests
import os

def review_code(diff):
    print("🤖 AI is reviewing code...")

    api_key = os.getenv("OPENROUTER_API_KEY")

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    prompt = f"""
You are a senior software engineer.

Review the following git diff and give concise feedback:
- bugs
- improvements
- best practices

Keep it short and clear.

Diff:
{diff}
"""

    data = {
        "model": "openai/gpt-4o-mini",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }

    try:
        response = requests.post(url, headers=headers, json=data)

        if response.status_code != 200:
            print("❌ AI Error:", response.status_code, response.text)
            return "AI review failed"

        result = response.json()
        return result["choices"][0]["message"]["content"]

    except Exception as e:
        print("❌ Exception:", e)
        return "AI review failed"