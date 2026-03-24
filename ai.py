from openai import OpenAI

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
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