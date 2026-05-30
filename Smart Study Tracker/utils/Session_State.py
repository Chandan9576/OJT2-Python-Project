import streamlit as st


DEFAULT_SESSION = {
    "page": "app",
    "logged_in": False,
    "current_user": None,
    "current_subject":None
}


def init_session():

    for key, value in DEFAULT_SESSION.items():

        if key not in st.session_state:
            st.session_state[key] = value


def navigate(page_name):

    st.session_state.page = page_name
    st.rerun()


def loginSession(current_user_data):

    st.session_state.logged_in = True
    st.session_state.current_user = current_user_data

def subjectSession(current_subject_data):
    st.session_state.current_subject = current_subject_data


def logout():

    st.session_state.logged_in = False
    st.session_state.current_user = None
    st.session_state.page = "app"
    st.switch_page("App.py")