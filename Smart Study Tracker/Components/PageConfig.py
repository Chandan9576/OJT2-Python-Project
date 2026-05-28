import streamlit as st

def show_PageConfig():
    st.set_page_config(
    page_title="Smart Study Tracker",
    page_icon="📚",
    layout="wide",  
)

def show_logo():
    st.logo("Assets/logo.png",size="large")