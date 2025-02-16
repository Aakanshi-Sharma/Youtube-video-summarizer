import os

import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import os

# --------------Utils-------------------
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))

# ----------------UI-----------------

st.set_page_config(page_title="Youtube Video Summarizer")
st.header("Youtube Video Transcript Summarizer")
