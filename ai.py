from dotenv import load_dotenv
import datetime
import re
from openai import OpenAI
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def save_filename(query, max_length=20): 
    filename = re.sub(r'[^\w\s-]', '', query)
    filename = filename.strip().replace(" ", '_')
    filename = filename[:max_length]
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    return f'{filename}_{timestamp}.txt'

def save_response(query, response):
    os.makedirs("ai_responses", exist_ok=True)
    filename = save_filename(query)
    filepath = os.path.join("ai_responses", filename)
    with open(filepath, 'w', encoding="utf-8") as f:
        f.write(f'USER QUERY:\n{query}\n\nAI RESPONSE:\n{response}')
    print(f'Saved AI response to {filepath}')