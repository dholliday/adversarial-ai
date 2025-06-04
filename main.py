from dotenv import load_dotenv
from openai import OpenAI
import anthropic
from google import genai
import os

load_dotenv(override=True)

gemini = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def main():
    response = gemini.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works in a few words"
    )
    print(response.text)


if __name__ == "__main__":
    main()
