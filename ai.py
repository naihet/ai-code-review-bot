from openai import OpenAI

client = OpenAI()

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
            model="gpt-4o-mini",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        result = response.choices[0].message.content
        return result

    except Exception as e:
        print("❌ AI Error:", e)
        return "AI review failed"