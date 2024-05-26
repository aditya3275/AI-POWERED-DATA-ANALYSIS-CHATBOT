import streamlit as st
import streamlit_option_menu as  option_menu
from home import home
from about import about
from pdf import pdf
from csvdata import csv
from excel import excel
from chat import chat
from pdfcontextbot import pdfcontextbot


def main():
    navigation = st.sidebar.selectbox("Menu", ["HOME","ABOUT","PDF DATA ANALYSIS","PDF CONTEXT CHAT BOT","CSV DATA ANALYSIS","CSV CONTEXT BOT", "EXCEL DATA ANALYSIS","CHAT WITH ME"])
    
    
    if navigation == "HOME":
        home()
    elif navigation == "ABOUT":
        about()
    elif navigation == "PDF DATA ANALYSIS":
        pdf()
    elif navigation == "PDF CONTEXT CHAT BOT":
        pdfcontextbot()
    elif navigation == "CSV DATA ANALYSIS":
        csv()
    elif navigation == "EXCEL DATA ANALYSIS":
        excel()
    elif navigation == "CHAT WITH ME":
        chat()
    


if  __name__ == "__main__":
    main()

    