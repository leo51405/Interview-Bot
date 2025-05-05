import google.generativeai as genai
from typing import List, Tuple
import gradio as gr
import json

# Set up Gemini API key
GOOGLE_API_KEY="AIzaSyD8d8foqTNUDIn4COLFnFre-cDkWdWbWdI"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro')

# 測試簡單 prompt
response = model.generate_content("我現在正在寫作業，可以鼓勵我嗎?")
print(response.text)
