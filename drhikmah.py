import streamlit as st
import openai

openai.api_key = "your_openrouter_api_key"

st.set_page_config(page_title="Dr. Hikmah", layout="centered")
st.title("🩺 Dr. Hikmah - Your AI Health Assistant")

st.markdown("Ask anything health-related. This is an AI helper, not a replacement for a doctor.")

user_input = st.text_input("What's your question?")

if user_input:
    with st.spinner("Thinking..."):
        response = openai.ChatCompletion.create(
            model="mistralai/mixtral-8x7b-instruct",
            messages=[
                {"role": "system", "content": "You are Dr. Hikmah, an Islamic AI health assistant. Be polite, professional, and cautious. Always mention that this is not real medical advice."},
                {"role": "user", "content": user_input}
            ]
        )
        st.write("**AI Doctor:**", response['choices'][0]['message']['content'])
