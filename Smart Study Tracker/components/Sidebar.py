import streamlit as st

def show_sidebar():

    st.sidebar.title("Smart Study Tracker")

    st.sidebar.write(
        f"Welcome {st.session_state.user['username']}"
    )

    st.sidebar.divider()

    if st.sidebar.button("Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()

    if st.sidebar.button("Subjects"):
        st.session_state.page = "subjects"
        st.rerun()

    if st.sidebar.button("Study Session"):
        st.session_state.page = "study_session"
        st.rerun()

    if st.sidebar.button("Analytics"):
        st.session_state.page = "analytics"
        st.rerun()

    st.sidebar.divider()

    if st.sidebar.button("Logout"):

        st.session_state.logged_in = False
        st.session_state.user = None
        st.session_state.page = "home"

        st.rerun()