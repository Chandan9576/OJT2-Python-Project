import streamlit as st
from Databases.Connection import users_collection
from Utils.Session_State import navigate
from Utils.Session_State import loginSession
from Components.PageConfig import show_logo
import random

def show_signin():

    show_logo()

    # ---------------- HEADER ----------------

  
    top_col1, top_col2 = st.columns([10, 2])

    with top_col1:
        st.title("📚 Smart Study Tracker")

    with top_col2:

        if st.button("🏠 Back to Home"):
            # st.session_state.page = "home"
            # st.rerun()
            navigate("app")

    st.divider()

    # ---------------- CENTER FORM ----------------

    left_space, center_col, right_space = st.columns([1, 2, 1])

    with center_col:

        st.markdown(
            """
            <h1 style='text-align: center;'>
                Welcome Back
            </h1>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <p style='text-align: center; color: gray; font-size:18px;'>
                Sign in to continue your learning journey
            </p>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        # -------------- form for handle the data ------------
        with st.form("SignIn form"):
            userName = st.text_input(
            "Username",
            placeholder="Enter your username")

            password = st.text_input(
                "Password",
                type="password",
                placeholder="Enter your password")

            st.write("")

            login_button = st.form_submit_button(
                "Sign In",
                use_container_width=True)

            if login_button:
                if (userName.strip() == "" or password.strip() == ""):
                    st.warning("Please fill all fields")

                else:

                    current_user = users_collection.find_one({"username":userName,"password":password})

                    if current_user:
                
                        st.session_state.current_user = {
                            "_id": current_user["_id"],
                            "username": current_user["username"],
                            "email": current_user["email"],
                            "full_name": current_user["full_name"]
                        }
                        loginSession(current_user)
                        st.success("Login successful")
                        st.switch_page("pages/dashboard.py")

                    else:
                        st.error("Invalid login details!!!")

            st.markdown(
                """
                <p style='text-align: center;'>
                    Don't have an account?
                </p>
                """,
                unsafe_allow_html=True
            )

            if st.form_submit_button("Create New Account",use_container_width=True):

                st.session_state.page = "signup"
                st.rerun()

            