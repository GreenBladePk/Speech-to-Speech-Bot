import streamlit as st
import openai
from voice import record_voice, text_to_speech
from openai import ChatCompletion
import time

openai.api_key = "API_KEY"

st.set_page_config(page_title="🎙️ Pk's Bot", layout="wide")

# Custom CSS for styling
custom_css = """
<style>
    body {
        background-color: #C6BADE; /* Light beige */
    }
    .main {
        background-color: #C6BADE; /* Light beige */
    }
    .stApp {
        background-color: #C6BADE;
    }
    .stTextInput, .stChatInput, .stButton, .stMarkdown {
        background-color: #DE638A; /* Dark beige */
        color:rgb(0, 0, 0); /* Text color */
        border-radius: 10px;
    }

    h1 {
        text-align: center; /* Center align title and text */
        background-color: #4A3267;
        color:rgb(0, 0, 0);
    } 
    .stMarkdown p {
        text-align: left; /* Center align title and text */
        color:rgb(0, 0, 0);
    }
    .stChatMessage {
        background-color: #DE638A; /* Chat bubbles dark beige */
        border-radius: 10px;
    }
    .stChatMessage .user {
        text-align: left;
    }
    .stChatMessage .assistant {
        text-align: left;
    }
    .center {
        display: flex;
        justify-content: center;
        align-items: left;
    }
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

st.markdown("<h1>🎙️ Speech to Speech Bot</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color:rgb(0, 0, 0);'>AI Assistant to help you !!!</p>", unsafe_allow_html=True)

# Function to interact with GPT-4 Mini
def get_gpt4_answer(question, context):
    prompt = f"Context: {context}\nQuestion: {question}\nAnswer:"

    response = openai.ChatCompletion.create(
        model="gpt-4",  
        messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=150
    )

    answer = response['choices'][0]['message']['content']
    return answer

def print_txt(text):
    st.markdown(f"<p style='color: rgb(0,0,0);'>{text}</p>", unsafe_allow_html=True)

def print_chat_message(message):
    text = message["content"]
    if message["role"] == "user":
        with st.chat_message("user", avatar="🎙️"):
            print_txt(text)
    else:
        with st.chat_message("assistant", avatar="🤖"):
            print_txt(text)

def main():
    st.markdown("<div class='center'>", unsafe_allow_html=True)
    question = record_voice(language="en") 
    st.markdown("</div>", unsafe_allow_html=True)

    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    chat_history = st.session_state.chat_history

    for message in chat_history:
        print_chat_message(message)

    if question:
        start = time.time()
        context = " ".join([msg['content'] for msg in chat_history])

        answer = get_gpt4_answer(question, context)

        end = time.time()
        print("Latency = ", end - start)
        user_message = {"role": "user", "content": question}
        print_chat_message(user_message)
        chat_history.append(user_message)

        ai_message = {"role": "assistant", "content": answer}
        print_chat_message(ai_message)
        chat_history.append(ai_message)

        text_to_speech(answer)
        
        if len(chat_history) > 20:
            chat_history = chat_history[-20:]

        st.session_state.chat_history = chat_history


if __name__ == "__main__":
    main()
