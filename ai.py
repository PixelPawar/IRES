from openai import OpenAI
from dotenv import load_dotenv
import os
import datetime
import re

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def ai_response(query):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful voice assistant."
                },
                {
                    "role": "user",
                    "content": query
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"AI Error: {e}"


def handle_ai_query(query):
    if "using ai" in query:
        from speech import say

        say("Consulting the AI, please wait...")

        response = ai_response(query)

        save_response(query, response)

        say(response)

        return True

    return False