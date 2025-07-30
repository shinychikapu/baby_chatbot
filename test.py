import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Optional: System prompt for GPT
system_prompt = """You are a kind, helpful assistant for a mom-baby support app.
Always be gentle and recommend that users consult a doctor for medical concerns."""

# Start conversation with a system message
messages = [{"role": "system", "content": system_prompt}]

print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ("exit", "quit"):
        print("Ending chat.")
        break

    messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="gpt-4.1",  # or "gpt-3.5-turbo"
            messages=messages,
        )
        reply = response.choices[0].message.content.strip()
        print("Bot:", reply)
        messages.append({"role": "assistant", "content": reply})
    except Exception as e:
        print("Error:", e)
