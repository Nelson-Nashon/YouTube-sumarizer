import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-3.6-flash")

def summarize(transcript: str, style: str = "concise") -> str:
    prompt = f"""Summarize the following YouTube video transcript.
Style: {style}
Include: main topic, 3-5 key points, and a one-line takeaway.

Transcript:
{transcript[:15000]}"""

    response = model.generate_content(prompt)
    return response.text