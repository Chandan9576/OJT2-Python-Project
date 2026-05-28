import streamlit as st
from Auth.Signin import show_signin
from Utils.Session_State import loginSession
from Utils.Session_State import subjectSession
from Utils.Session_State import navigate
from Components.PageConfig import show_PageConfig,show_logo
from Databases.Connection import subjects_collection
from Utils.Analytics import get_total_completed_topics
from Utils.Analytics import get_total_topics
from Utils.Analytics import get_total_subject
from Utils.Analytics import get_total_subject_topics
from Utils.Analytics import get_total_copleted_subject_topics
from Utils.Analytics import get_subject_wise_progress
from Utils.Analytics import get_total_completed_subjects



show_PageConfig()

show_logo()

st.session_state.page = "app"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in==True:

    st.title("📗 Your Subject")
    st.caption(
        "Manage and organize your learning subjects"
    )

    # ----------- SUBJECT INFROMATION ---------

    info1,info2,info3 = st.columns(3)

    with info1:
        with st.container(border=True):
            st.info(f"Total Subjects :- {get_total_subject(st.session_state.current_user["_id"])}")

    with info2:
        with st.container(border=True):
            st.success(f"✅ Completed Subject :- {get_total_completed_subjects(st.session_state.current_user["_id"])}")

    with info3:
        with st.container(border=True):
            st.warning(f"🟡 Pending Subject :- {get_total_subject(st.session_state.current_user["_id"])-get_total_completed_subjects(st.session_state.current_user["_id"])}")
    

    # ---------- ADD SUBJECT SECTION ----------

    with st.container(border=True):

        st.subheader("➕ Add New Subject")

        subject_name = st.text_input(
            "Subject Name",
            placeholder="Enter subject name"
        )

        if st.button("Add Subject",use_container_width=True):

            if subject_name.strip() == "":
                st.warning("Please enter subject name")

            else:
                # Check duplicate subject
                existing_subject = subjects_collection.find_one({

                    "user_id": st.session_state.current_user["_id"],

                    "subject_name": subject_name
                })

                if existing_subject:

                    st.error("Subject already exists")

                else:

                    subject_data = {
                        "user_id": st.session_state.current_user["_id"],
                        "subject_name": subject_name
                    }

                    subjects_collection.insert_one(subject_data)
                    st.success("Subject Added Successfully")
                    st.rerun()

    st.write("")

    # ---------- DISPLAY SUBJECTS ----------

    st.header("📘 Your Subjects")

    # fetching total subject list of current user
    subjects = list(subjects_collection.find({
        "user_id": st.session_state.current_user["_id"]
    }))

    if len(subjects) == 0:
        st.info("No subjects added yet")

    else:

        col1, col2, col3 = st.columns(3)

        columns = [col1, col2, col3]

        for index, subject in enumerate(subjects):

            with columns[index % 3]:

                with st.container(border=True):
                    st.subheader(f"📘 {subject['subject_name']}")

                    # ------ Total subject topics ------------

                    st.write(f"Total Topics : {get_total_subject_topics(st.session_state.current_user["_id"],subject["_id"])}")

                    # ------- Total completed subject topics ----

                    st.write(f"Completed Topics : {get_total_copleted_subject_topics(st.session_state.current_user["_id"],subject["_id"])}")

                    # -------- Subject wise progress --------

                    total_topics = get_total_subject_topics(
                        st.session_state.current_user["_id"],
                        subject["_id"]
                    )

                    completed_topics = get_total_copleted_subject_topics(
                        st.session_state.current_user["_id"],
                        subject["_id"]
                    )

                    if total_topics > 0:
                        progress_percentage = (
                            completed_topics / total_topics
                        ) * 100

                    else:
                        progress_percentage = 0

                    st.write(f"Progress : {progress_percentage:.2f}%")

                    st.progress(progress_percentage / 100)

                    st.write("")

                    btn_col1, btn_col2 = st.columns(2)

                    # ----- OPEN BUTTON -----

                    with btn_col1:

                        if st.button("Open",key=f"open_{subject['_id']}",use_container_width=True):

                            st.session_state.current_subject = {
                                "_id": subject["_id"],
                                "subject_name": subject["subject_name"]
                            }

                            st.switch_page("Pages/Chapter.py")
                        

                    # ----- DELETE BUTTON -----

                    with btn_col2:

                        if st.button("❌ Delete",key=f"delete_{subject ['_id']}",use_container_width=True):

                            subjects_collection.delete_one({
                                "_id": subject["_id"]
                            })

                            st.success("Subject Deleted")

                            st.rerun()

else:
    dash_col1, dash_col2 = st.columns([7, 2])

    with dash_col1:
        st.title("📗 Subject")
        st.warning("Please SigIn first!!!")

    with dash_col2:
        if st.button("🔑 Sign In"):
            st.session_state.page="signin"
            st.switch_page("App.py")