from openai import OpenAI
import os

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def review_code(diff):
    print("🤖 AI is reviewing code...")

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

    try:
        response = client.chat.completions.create(
            model="mistralai/mistral-7b-instruct",

            messages=[
                {"role": "user", "content": prompt}
            ],

            temperature=0.3
        )

        return response.choices[0].message.content

    except Exception as e:
        print("❌ AI Error:", e)
        return "AI review failed"