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


def extract_transcript_url(youtube_url):
    try:
        video_id = youtube_url.split("=")[-1]
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = ""
        for i in transcript:
            text += " " + i["text"]
        return text
    except Exception as e:
        raise e


prompt = """
You are youtube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 250 words.Provide the summary of the text given here : 
"""

# ----------------UI-----------------

st.set_page_config(page_title="Youtube Video Summarizer")
st.header("Youtube Video Transcript Summarizer")
link = st.text_input("Enter the link")
if link:
    video_id = link.split("=")[-1]
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_container_width=True)
submit_button = st.button("Summarize")
if submit_button:
    extracted_text = extract_transcript_url(link)
    if extracted_text:
        result = generate_gemini_content(extracted_text, prompt)
        st.write(result)
