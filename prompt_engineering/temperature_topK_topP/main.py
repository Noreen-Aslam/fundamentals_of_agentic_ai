import os
from dotenv import load_dotenv
import google.generativeai as genai

# load .env file
load_dotenv()

# Api key
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=api_key)

# Select model
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Prompt
prompt = "Write a short story about a cat learning programming"

# Generate content with Temperature, Top-k and Top-p
response = model.generate_content(
    prompt,
    generation_config={
        "temperature": 0.7, # medium creativity
        "top_k": 20,        # Consider top 20 words
        "top_p": 0.9        # Consider words covering 90% probability
    }

)

print (response.text)

