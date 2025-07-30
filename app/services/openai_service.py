from fastapi import HTTPException
from openai import OpenAI
from app.core.config import OPENAI_API_KEY

# Create OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Global in-memory chat history
chat_history = []

def load_system_prompt():
    try:
        with open("app/prompts/base_prompt.txt", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print("⚠️ Failed to load system prompt:", e)
        return "You are a helpful and friendly assistant in a mom-baby support app."

async def get_openai_response(user_message: str):
    try:
        system_prompt = load_system_prompt()
        chat_history.append({"role": "user", "content": user_message})

        messages = [{"role": "system", "content": system_prompt}] + chat_history

        # ✅ Use new SDK interface
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        reply = response.choices[0].message.content.strip()

        chat_history.append({"role": "assistant", "content": reply})

        return reply, chat_history[-20:]

    except Exception as e:
        print("❌ OpenAI API error:", str(e))
        raise HTTPException(status_code=500, detail=f"OpenAI API error: {str(e)}")
