# app.py
import streamlit as st
from auth.Signin import show_signin
from auth.Signup import show_signup
# from Pages.Dashboard import show_dashboard
from utils.Session_State import init_session
from utils.Session_State import navigate
from components.PageConfig import show_PageConfig,show_logo
from pathlib import Path

show_PageConfig()

show_logo()
#----------------- PAGE STATE ---------------

init_session()


# ---------------- HOME PAGE ----------------

if st.session_state.page == "app":

    # ---------------- HEADER ----------------

    col1, col2 = st.columns([7, 2])

    with col1:
        st.title("📚 Smart Study Tracker")

    with col2:

        btn_col1, btn_col2 = st.columns(2)

        with btn_col1:

            if st.button("🔑 Sign In"):
                # st.session_state["page"] = "signin"
                # st.rerun()
                navigate("signin")

        with btn_col2:

            if st.button("🔐 Sign Up"):
                # st.session_state["page"] = "signup"
                # st.rerun()
                navigate("signup")

    st.divider()

    # ---------------- HERO SECTION ----------------

    left_col, right_col = st.columns(2)

    with left_col:

        st.markdown("## Track Your Learning Journey Smarter")

        st.markdown(
            """
            ### Manage your learning journey in one organized workspace.
            
            Track subjects, monitor progress, build study consistency,
            and gain meaningful insights into your learning habits through
            a smart productivity dashboard designed for students and self-learners.
            """
        )

        col_a, col_b, col_c = st.columns(3)

        with col_a:
            st.button("🚀 Get Started")

        with col_b:
            st.button("📖 Learn More")

    with right_col:

        BASE_DIR = Path(__file__).resolve().parent
        image_path = BASE_DIR / "assets" / "image.png"
        st.image(str(image_path),use_container_width=True)

    st.divider()

    # ---------------- FEATURES ----------------

    st.markdown("## ✨ Features")

    feature1, feature2, feature3 = st.columns(3)

    with feature1:

        st.info("📘 Topic Tracking")
        st.write(
            "Manage subjects and track completed topics easily."
        )

    with feature2:

        st.success("📊 Smart Analytics")
        st.write(
            "Visualize your learning consistency and study trends."
        )

    with feature3:

        st.warning("⚡ Productivity System")
        st.write(
            "Build strong study habits with structured planning."
        )

    st.divider()

    # ---------------- ANALYTICS PREVIEW ----------------

    # st.markdown("## 📈 Analytics Preview")

    # metric1, metric2, metric3 = st.columns(3)

    # with metric1:
    #     st.metric("Subjects", "8")

    # with metric2:
    #     st.metric("Study Streak", "12 Days")

    # with metric3:
    #     st.metric("Topics Completed", "143")

    # st.divider()

    # ---------------- FOOTER ----------------

    st.markdown(
        """
        <center>
            <p>Smart Study Tracker © 2026</p>
            <p>Built with Streamlit & Python</p>
        </center>
        """,
        unsafe_allow_html=True
    )


# ---------------- SIGN IN PAGE STATE ----------------

elif st.session_state.page == "signin":
    show_signin()


# ---------------- SIGN UP PAGE STATE ----------------

elif st.session_state.page == "signup":
    show_signup()

#----------------- Dashboard page state --------------

# elif st.session_state.page == "dashboard":
#     show_dashboard()

