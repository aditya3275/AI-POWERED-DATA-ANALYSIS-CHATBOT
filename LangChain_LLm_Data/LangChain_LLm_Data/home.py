import streamlit as st
import os

def home():
    st.markdown("<h1 style='text-align: center; color: white;'>Discover the power of Genesis AI</h1>", unsafe_allow_html=True)

    st.subheader("🚀 Welcome to Genesis AI: Your Intelligent Data Analysis Companion! 🤖")
    st.write("Have questions about your data? Need insightful analysis in seconds? You're in the right place!")
    st.write("Ask Genesis AI anything about your CSV, Excel, or PDF files. From trend analysis to contextual understanding, Genesis AI has got you covered.")
    st.write("Simply upload your files and start chatting. Let's unlock the power of AI together! 💡")

    st.image(r"..\LangChain_LLm_Data\images\main pic.jpg")
    
    st.header("Why Choose Genesis AI?")
    st.write("1. Instant Insights: Get actionable insights from your data in real-time.")
    st.write("2. Versatile Analysis: Analyze CSV, Excel, or PDF files effortlessly.")
    st.write("3. Conversational AI: Chat with Genesis AI to explore your data in a natural way.")
    st.write("4. User-Friendly: Easy-to-use interface for seamless interaction.")
    st.write("5. Powerful AI: Leveraging cutting-edge AI technology for accurate analysis.")


    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            bottom: 0;
            width: 42%;
            background-color: #000000;
            text-align: center;
            padding: 10px 0;
        }
        </style>
        <div class="footer">
            Powered by Genesis AI ©️ 2024
        </div>
        """,
        unsafe_allow_html=True
    )


