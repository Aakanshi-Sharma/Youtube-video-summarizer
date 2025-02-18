import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import os
from youtube_transcript_api import YouTubeTranscriptApi

# --------------Utils-------------------
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))


# --------------Functions--------------
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt + transcript_text)
    return response.text


prompt = """
You are youtube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 250 words. The transcript text will be appended here : 
"""

# ----------------UI-----------------

st.set_page_config(page_title="Youtube Video Summarizer")
st.header("Youtube Video Transcript Summarizer")
link=st.text_input("Enter the link")