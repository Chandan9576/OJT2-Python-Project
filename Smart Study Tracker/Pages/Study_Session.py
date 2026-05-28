import streamlit as st
from Auth.Signin import show_signin
from Utils.Session_State import loginSession
from Utils.Session_State import navigate
from Components.PageConfig import show_PageConfig,show_logo

show_PageConfig()

st.session_state.page = "app"
show_logo()

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in==True:

    #------------- HEADER ----------------
    st.title(f"🧑‍💻 {st.session_state.current_user['username']}'s Study Session")
    st.caption(
        "Focus on consistency, not intensity."
    )
    st.divider()


    # ---------- SUBJECT & TOPIC SELECTION ----------

    select_col1, select_col2 = st.columns(2)

    with select_col1:

        selected_subject = st.selectbox(

            "📘 Select Subject",

            [
                "Physics",
                "DSA",
                "DBMS",
                "Python"
            ]
        )

    with select_col2:

        selected_topic = st.selectbox(

            "📖 Select Topic",

            [
                "Motion",
                "Recursion",
                "Normalization",
                "Functions"
            ]
        )


    st.write("")
    st.divider()


    # ---------- TIMER SECTION ----------

    timer_col1, timer_col2, timer_col3 = st.columns([1, 2, 1])

    with timer_col2:

        with st.container(border=True):

            st.markdown(
                "<h3 style='text-align:center;'>⏱ Focus Timer</h3>",
                unsafe_allow_html=True
            )

            st.markdown(
                """
                <h1 style='
                    text-align:center;
                    font-size:70px;
                    margin-top:20px;
                    margin-bottom:20px;
                '>
                00:25:18
                </h1>
                """,
                unsafe_allow_html=True
            )

            btn_col1, btn_col2, btn_col3 = st.columns(3)

            with btn_col1:

                st.button(
                    "▶ Start",
                    use_container_width=True
                )

            with btn_col2:

                st.button(
                    "⏸ Pause",
                    use_container_width=True
                )

            with btn_col3:

                st.button(
                    "⏹ End",
                    use_container_width=True
                )


    st.write("")
    st.divider()


    # ---------- SESSION STATS ----------

    st.subheader("📊 Session Stats")

    stats_col1, stats_col2, stats_col3 = st.columns(3)

    with stats_col1:

        with st.container(border=True):

            st.metric(
                "📚 Study Today",
                "2h 10m"
            )

    with stats_col2:

        with st.container(border=True):

            st.metric(
                "🔥 Current Streak",
                "5 Days"
            )

    with stats_col3:

        with st.container(border=True):

            st.metric(
                "🧠 Sessions Today",
                "4"
            )


    st.write("")
    st.divider()


    # ---------- TODAY'S STUDY LOG ----------

    st.subheader("📌 Today's Study Log")

    with st.container(border=True):

        st.write("📘 Physics → Optics → 45 mins")

        st.write("💻 DSA → Recursion → 30 mins")

        st.write("🐍 Python → Functions → 25 mins")


    st.write("")
    st.divider()


    # ---------- MOTIVATION FOOTER ----------

    st.markdown(
        """
        <h4 style='text-align:center; color:gray;'>
        Small daily progress beats random motivation.
        </h4>
        """,
        unsafe_allow_html=True
    )
else:
    dash_col1, dash_col2 = st.columns([7, 2])

    with dash_col1:
        st.title("🧑‍💻 Study Session")
        st.warning("Please SigIn first!!!")

    with dash_col2:
        if st.button("🔑 Sign In"):
            st.session_state.page="signin"
            st.switch_page("App.py")