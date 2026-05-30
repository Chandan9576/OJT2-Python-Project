import streamlit as st
from PIL import Image
from pathlib import Path

def show_PageConfig():
    st.set_page_config(
    page_title="Smart Study Tracker",
    page_icon="📚",
    layout="wide",  
)

def show_logo():
    BASE_DIR = Path(__file__).resolve().parent.parent

    logo_path = BASE_DIR / "Assets" / "logo.png"

    logo = Image.open(logo_path)

    st.logo(logo, size="large")