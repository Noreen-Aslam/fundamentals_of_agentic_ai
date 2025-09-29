import os
from dotenv import load_dotenv
import google.generativeai as genai

# .env file se API key load karo
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Gemini ko configure karo
genai.configure(api_key=api_key)

# Model select karo
model = genai.GenerativeModel("gemini-2.0-flash")

# Chain of Thought prompt
prompt = """
Question: Ali has 3 apples, and he buys 2 more. How many apples does he have in total?

Solve this step by step before giving the final answer.
"""

# Content generate karo
response = model.generate_content(prompt)

# Result print karo
print(response.text)
