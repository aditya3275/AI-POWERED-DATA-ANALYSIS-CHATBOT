import streamlit as st

def about():
    st.title("Know About Us!!")
    st.write("Genesis AI is revolutionizing the way data analysis is done. Our team is dedicated to providing cutting-edge AI solutions to empower businesses and individuals to make informed decisions based on data-driven insights.")

    st.header("Our Mission")
    st.write("Our mission is to democratize access to advanced data analysis tools and technologies. We aim to make sophisticated data analysis techniques accessible to everyone, regardless of their technical background.")

    st.header("Chatbot: Your Data Analysis Companion")
    st.write("Our AI-powered chatbot is designed to assist you with data analysis tasks in a conversational manner. Here's how it works:")
    st.markdown("- **Upload Files**: Start by uploading your CSV, Excel, or PDF files containing the data you want to analyze.")
    st.markdown("- **CSV Data Analysis**: Upload CSV files to analyze structured tabular data. Ask questions about specific columns, rows, trends, or patterns.")
    st.markdown("- **Excel Data Analysis**: Upload Excel files to perform in-depth analysis of spreadsheets. Query data, calculate metrics, or visualize trends.")
    st.markdown("- **PDF Data Analysis**: Upload PDF files to extract text and insights. Explore textual data, extract key information, or analyze document contents.")
    st.markdown("- **Conversational AI**: Engage in a conversation with the chatbot to explore your data further. Ask follow-up questions, refine your queries, or request additional analysis.")
    st.markdown("- **Contextual Understanding**: The chatbot adapts its responses based on the type of file uploaded and the context of your questions.")

    # Add footer with CSS for fixed positioning
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

# You can then call the about function in your main app.py file
