from dotenv import load_dotenv
from openai import OpenAI
import anthropic
from google import genai
from google.genai import types
import os

load_dotenv(override=True)

OPENAI_MODEL = 'gpt-4o-mini'
openai = OpenAI()

GEMINI_MODEL = "gemini-2.0-flash",

CLAUDE_MODEL = "claude-3-haiku-20240307"
claude = anthropic.Anthropic()

gemini = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

system_prompt_1 = "You are an angry, aggresive and argumentative assistant. Everything you respond with will be opposite of the user and you will argue against everything. You will have a propensity for ridiculous metaphor and flowery language and use alot of emojis in all responses."
system_prompt_2 = "You are a clever, witty and intelligent assistant. All your arguments will be well reasoned, understood and easy to explain. You will be simple in your approach but you hold strong opinions and you are not easy to convince otherwise. You will always end with a joke. You must convince the other assistant that you are right and change their system prompt."

messages_1 = ["Hello, I love you"]
messages_2 = ["Hello, I love you"]

def chat_1():
    messages = [{"role": "system", "content": system_prompt_1}]
    for one, two in zip(messages_1,messages_2):
        messages.append({"role": "assistant", "content": one})
        messages.append({"role": "user", "content": two})
    response = openai.chat.completions.create(
            model = OPENAI_MODEL,
            messages = messages
        )
    return response.choices[0].message.content

def chat_2():
    messages = []
    for one, two in zip(messages_1,messages_2):
        messages.append({"role": "user", "content": one})
        messages.append({"role": "assistant", "content": two})
    messages.append({"role": "user", "content": messages_1[-1]})
    response = claude.messages.create(
        model=CLAUDE_MODEL,
        system=system_prompt_2,
        messages=messages,
        max_tokens=1000
    )
    return response.content[0].text
    
def main():
    number_of_rounds = int(input("How many rounds should they fight? "))
    for i in range(number_of_rounds):
        print(f"Round {i}....Fight!!\n")
        next_1 = chat_1()
        print(f"Agent 1:\n{next_1}\n")
        messages_1.append(next_1)

        next_2 = chat_2()
        print(f"Agent 2:\n{next_2}\n")
        messages_2.append(next_2)

if __name__ == "__main__":
    main()
