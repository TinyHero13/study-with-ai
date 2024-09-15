from litellm import completion
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')

def user_prompt(guide, prompt):
    response = completion(
        model="groq/llama3-8b-8192", 
        messages=[
        {"role": "user", "content": f"Escreva toda a resposta em português {guide}{prompt}"}
    ],
    )
    return response['choices'][0]['message']['content']