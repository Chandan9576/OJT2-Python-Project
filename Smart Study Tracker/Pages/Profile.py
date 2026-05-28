import streamlit as st
from Auth.Signin import show_signin
from Utils.Session_State import logout
from Utils.Session_State import navigate
from Components.PageConfig import show_PageConfig,show_logo

show_PageConfig()

st.session_state.page = "app"
show_logo()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in==True:
    dash_col1, dash_col2 = st.columns([7,2])
    with dash_col1:
        # username = st.session_state.get('current_user')
        # st.write(username)

        st.title(f"👤 Welcome {st.session_state.current_user['username']}")

    with dash_col2:
        if st.button("🔒 Logout"):
            logout()

else:
    dash_col1, dash_col2 = st.columns([7, 2])

    with dash_col1:
        st.title("👤 No Profile")
        st.warning("Please SigIn first!!!")

    with dash_col2:
        if st.button("🔑 Sign In"):
            st.session_state.page="signin"
            st.switch_page("App.py")