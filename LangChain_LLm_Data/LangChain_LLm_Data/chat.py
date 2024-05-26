import streamlit as st
import os
import google.generativeai as genai

# Configure Google API
GOOGLE_API_KEY = "API-KEY"
genai.configure(api_key=GOOGLE_API_KEY)

def chat():
    # Function to load Gemini Pro model and get responses
    model = genai.GenerativeModel("gemini-pro") 
    chat = model.start_chat(history=[])

    def get_gemini_response(question):
        response = chat.send_message(question, stream=True)
        return response

    # Initialize Streamlit app
    st.title("Gemini LLM Application")

    # Initialize session state for chat history if it doesn't exist
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    # Sidebar
    st.sidebar.title("Instructions")
    st.sidebar.markdown(
        "1. Input your question in the text box below.\n"
        "2. Click on the 'Ask' button to get a response.\n"
        "3. View chat history on the right side."
    )

    # Main content area
    input_text = st.text_input("Input your question:", key="input")
    submit_button = st.button("Ask")

    if submit_button and input_text:
        response = get_gemini_response(input_text)
        st.session_state['chat_history'].append(("You", input_text))
        st.subheader("Response:")
        for chunk in response:
            st.write(chunk.text)
            st.session_state['chat_history'].append(("Bot", chunk.text))

    # # Chat history
    # st.sidebar.title("Chat History")
    # chat_history = st.sidebar.empty()
    # for role, text in st.session_state['chat_history']:
    #     chat_history.write(f"**{role}:** {text}")

    # Apply some styling
    st.markdown(
        """
        <style>
            .sidebar .sidebar-content {
                background-color: #f0f2f6;
            }
            .sidebar .sidebar-content .block-container {
                padding: 0px 20px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
