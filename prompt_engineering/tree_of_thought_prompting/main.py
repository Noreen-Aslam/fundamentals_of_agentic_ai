import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load the .env file where GEMINI_API_KEY is stored
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")  # Get the API key

# Configure Gemini API
genai.configure(api_key=api_key)

# Select the model (use available Gemini model)
model = genai.GenerativeModel("gemini-2.0-flash")

# Chain of Thought prompt
prompt = """
Question: Ali has 3 apples, and he buys 2 more. How many apples does he have in total?

Solve this step by step before giving the final answer.
"""

# Generate content from the model
response = model.generate_content(prompt)

# Print the AI's reasoning and answer
print(response.text)
