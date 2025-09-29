import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv( "GEMINI_API_KEY")

genai.configure(api_key=api_key)

model= genai.GenerativeModel("gemini-1.5-flash")

prompt = """
Make a markdown list of 3 benifits of learning python and every point should be in two to three line and every time will give new response"""
response = model.generate_content(prompt)

print(response.text)



