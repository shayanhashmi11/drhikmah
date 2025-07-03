import streamlit as st
from openai import OpenAI
import os

# Page setup
st.set_page_config(
    page_title="Dr. Hikmah - AI Health Assistant",
    page_icon="🩺",
    layout="centered"
)

# Title & description
st.title("🩺 Dr. Hikmah")
st.markdown("Welcome to **Dr. Hikmah**, your AI-powered general health assistant. Ask questions about symptoms, wellness, or fitness — and get safe, friendly guidance.\n\n⚠️ *Note: This AI does not diagnose or treat medical conditions. Always consult a licensed doctor for serious issues.*")

# Get API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Input field
user_input = st.text_input("🧠 Ask me something about your health:")

# Handle response
if user_input:
    with st.spinner("Thinking like a wise doctor..."):
        try:
            response = client.chat.completions.create(
                model="gpt-4",  # You can change to gpt-3.5-turbo if needed
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are Dr. Hikmah, an AI doctor created to provide helpful, calm, and informative advice. "
                            "You never diagnose, prescribe, or replace real doctors. Always recommend professional medical consultation for serious symptoms. "
                            "Respond clearly, kindly, and in simple language."
                        )
                    },
                    {"role": "user", "content": user_input}
                ]
            )

            st.success(response.choices[0].message.content)

        except Exception as e:
            st.error("❌ Something went wrong. Please try again later.")
            st.stop()
