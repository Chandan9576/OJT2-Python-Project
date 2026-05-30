import streamlit as st
from auth.Signin import show_signin
from utils.Session_State import loginSession
from utils.Session_State import navigate
from components.PageConfig import show_PageConfig,show_logo

show_PageConfig()

st.session_state.page = "app"
show_logo()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in==True:
    st.title(f"📖 {st.session_state.current_user['username']}'s Analytics")

    st.write("Analytics Page Comming Soon......")

else:
    dash_col1, dash_col2 = st.columns([7, 2])

    with dash_col1:
        st.title("📖 Analytics")
        st.warning("Please SigIn first!!!")

    with dash_col2:
        if st.button("🔑 Sign In"):
            st.session_state.page="signin"
            st.switch_page("App.py")