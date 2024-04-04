from dotenv import load_dotenv
load_dotenv() ## loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("AIzaSyCxgL_nohM3A9yDX0DsVB0ORxWv-7lKjj8"))

## function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-pro") 
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

## Initialize our Streamlit app
st.set_page_config(page_title="BOT PRO", layout="wide")

# Add background image using CSS and center-align all items
st.markdown(
    """
    <style>
    body {
        background-image: url("https://example.com/background_image.jpg");
        background-size: cover;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.header("BOT PRO")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

input_text = st.text_input("What's up! What do you need? Type here", key="input")
submit_button = st.button("Enter")
show_history_button = st.button("Show Chat History")

if submit_button and input_text:
    response = get_gemini_response(input_text)
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input_text))
    st.subheader("Answer for your queries:")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

if show_history_button:
    st.subheader("Your Chat History:") 
    for role, text in st.session_state['chat_history']:
        st.write(f"{role}: {text}")

