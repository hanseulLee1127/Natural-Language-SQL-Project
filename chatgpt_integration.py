import openai
import os
from dotenv import load_dotenv

# Load API key from environment
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_menu_recommendation_from_gpt(menu_name):
    prompt = f"Can you describe the Korean dish called '{menu_name}' in detail?"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']


