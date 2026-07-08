import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_answer(context: str, question: str):

    prompt = f"""
You are an intelligent AI assistant.

Answer ONLY using the provided context.

If the answer is not found in the context,
reply with:

'I couldn't find that information in the uploaded document.'

Context:
{context}

Question:
{question}
"""

    response = model.generate_content(prompt)

    return response.text