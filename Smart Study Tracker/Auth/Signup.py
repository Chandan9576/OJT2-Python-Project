import streamlit as st
from databases.Connection import users_collection
from utils.Session_State import navigate
from components.PageConfig import show_logo

def show_signup():

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
            <h2 style='text-align: center;'>
                Create Your Account
            </h2>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <p style='text-align: center; color: gray; font-size:18px;'>
                Start organizing your learning journey today
            </p>
            """,
            unsafe_allow_html=True
        )

        # ------------ SignUp form for handle the data -----------\

        with st.form("SignUp form"):

            full_name = st.text_input(
            "Full Name",
            placeholder="Enter your full name")

            username = st.text_input("Username",placeholder="Choose a username")

            email = st.text_input("Email Address",placeholder="Enter your email")

            password = st.text_input("Password",type="password",placeholder="Create password")

            confirm_password = st.text_input("Confirm Password",type="password",placeholder="Confirm password")

            st.write("")

            signup_button = st.form_submit_button("Create Account", use_container_width=True)

            # ---------------- SIGNUP LOGIC ----------------

            if signup_button:
                # Empty field validation
                if (full_name.strip() == "" or username.strip() == "" or email.strip() == "" or password.strip() == "" or  confirm_password.strip() == ""):
                    st.warning("All fields are required")

                # Password validation
                elif password != confirm_password:
                    st.error("Passwords do not match")

                else:
                    # Check existing email
                    existing_user = users_collection.find_one(
                        {"email": email})

                    if existing_user:
                        st.error("Email already registered")

                    else:
                        # User document
                        user_data = {

                            "full_name": full_name,
                            "username": username,
                            "email": email,
                            "password": password
                        }

                        # Insert into MongoDB
                        users_collection.insert_one(user_data)
                        st.success("Account created successfully")
                    

            st.markdown(
                """
                <p style='text-align: center;'>
                    Already have an account?
                </p>
                """,
                unsafe_allow_html=True
            )

            if st.form_submit_button("Go To Sign In",use_container_width=True):
                st.session_state.page = "signin"
                st.rerun()