import streamlit as st
from PIL import Image

def show_PageConfig():
    st.set_page_config(
    page_title="Smart Study Tracker",
    page_icon="📚",
    layout="wide",  
)

def show_logo():
    logo = Image.open("Assets/logo.png")
    st.logo(logo, size="large")