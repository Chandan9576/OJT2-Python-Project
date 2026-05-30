import streamlit as st
from auth.Signin import show_signin
from utils.Session_State import loginSession
from utils.Session_State import navigate
from components.PageConfig import show_PageConfig,show_logo
from databases.Connection import subjects_collection
from databases.Connection import topics_collection
from utils.Analytics import get_total_completed_chapter
from utils.Analytics import get_total_chapter
from utils.Analytics import get_total_subject
from utils.Analytics import get_total_subject_chapter
from utils.Analytics import get_total_copleted_subject_chapter
from utils.Analytics import get_subject_wise_progress
from utils.Avtivity import get_recent_activity


show_PageConfig()
st.session_state.page = "app"
show_logo()


if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


# -------------- Pages code start from here ---------------

if st.session_state.logged_in==True:

    # store session from Session_State page after login
    current_user_id = st.session_state.current_user["_id"]
    # current_subject_name = st.session_state.current_subject["subject_name"]
    # st.write(current_subject_name)
    # current_subject_id = st.session_state.current_subject["_id"]

    st.title(f"📒 Good Morning, {st.session_state.current_user['username']}")
    st.caption(
        "Track your study progress and stay consistent."
    )

    # ---------- STATS CARDS ----------

    col1, col2, col3, col4 = st.columns(4)

    # ----- CARD 1 Subjects -----

    with col1:

        with st.container(border=True):

            st.subheader("📚 Total Subjects")

            st.caption("Total active subjects")

            st.title(get_total_subject(current_user_id))

    # ----- CARD 2 Study hours-----

    with col2:

        with st.container(border=True):

            st.subheader("❇️ Total topics")

            st.caption("Total Topics")

            st.title(get_total_chapter(current_user_id))

    # ----- CARD 3 Total Topics -----

    with col3:

        with st.container(border=True):
            st.subheader("✅ Completed Topics")
            st.caption("Completed topics")
            st.title(get_total_completed_chapter(current_user_id))

    # ----- CARD 4 Strak -----

    with col4:

        with st.container(border=True):

            st.subheader("🔥 Streak")

            st.caption("Current study streak")

            st.title("0")

    st.write("")

    # ---------- GOAL & STREAK SECTION ----------

    left_col, right_col = st.columns(2)

    # ----- TODAY GOAL -----

    with left_col:

        with st.container(border=True):

            st.subheader("🎯 Today's Goal")
            st.write("")
            st.write("Target Study Hours : 4 Hours")
            st.write("Completed : 0 Hours")
            st.write("Remaining : 4 Hours")
            st.progress(0)

    # ----- STUDY STREAK -----

    with right_col:

        with st.container(border=True):
            st.subheader("🔥 Study Streak")
            st.write("")
            st.write("Current Streak : 0 Days")
            st.write("Best Streak : 0 Days")
            st.write("Stay consistent to grow your streak!")
            st.progress(0)

    st.write("")


    # ---------- PROGRESS OVERVIEW ----------

    with st.container(border=True):
        st.subheader("📈 Progress Overview")
        st.write("")
        if get_total_chapter(current_user_id) > 0:
            progress_percentage = (get_total_completed_chapter(current_user_id) / get_total_chapter(current_user_id)) * 100
            st.info(f"{progress_percentage:.2f} %")
            st.progress(progress_percentage / 100)
        else:
            st.write("0")


    # ---------- RECENT ACTIVITY ----------

    st.subheader("📌 Recent Activity")

    recent_activities = get_recent_activity(current_user_id)

    if len(recent_activities) == 0:

        st.info("No recent activity found")

    else:

        for activity in recent_activities:

            with st.container(border=True):

                st.write(

                    f"✅ {activity['message']}"
                )

                formatted_time = activity["created_at"].strftime("%d %b %Y • %I:%M %p")

                st.caption(
                    formatted_time
                )

else:
    dash_col1, dash_col2 = st.columns([7, 2])

    with dash_col1:
        st.title("📑 Dashboard")
        st.warning("Please SigIn first!!!")

    with dash_col2:
        if st.button("🔑 Sign In"):
            st.session_state.page="signin"
            st.switch_page("App.py")
            

    