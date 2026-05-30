import streamlit as st
from Auth.Signin import show_signin
from Utils.Session_State import loginSession
from Utils.Session_State import navigate
from Components.PageConfig import show_PageConfig,show_logo
from Databases.Connection import subjects_collection
from Databases.Connection import topics_collection
from Utils.Analytics import get_total_subject_chapter
from Utils.Analytics import get_total_copleted_subject_chapter
from Utils.Analytics import get_subject_wise_progress
from Utils.Avtivity import add_activity
import time

show_PageConfig()

show_logo()

st.session_state.page = "app"

# if "current_subject" not in st.session_state:
#     st.session_state.current_subject = None

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in==True:

    # ---------- GET CURRENT SUBJECT ----------

    if ("current_subject" not in st.session_state or st.  session_state.current_subject is None):
        st.warning("Please select a subject first")
        if st.button("⬅️ Back To Subjects"):
            st.switch_page("Pages/Subject.py")

        st.stop()

    current_subject = st.session_state.current_subject
    current_subject_id = current_subject["_id"]
    current_subject_name = current_subject["subject_name"]
    current_user = st.session_state.current_user
    current_user_id = current_user["_id"]


    # ---------- PAGE HEADER ----------

    st.title(f"📘 Your Chapter : {current_subject_name}")

    st.caption(
        "Manage and track your learning topics"
    )

    # ---------- BACK TP SUBJECT PAGE --------
    if st.button("⬅️ Back To Subjects"):
        st.switch_page("Pages/Subject.py")

    
        

    st.write("")

    # ----------- INFORMATION OF CHAPTER -----------

    info1,info2,info3 = st.columns(3)

    with info1:
        with st.container(border=True):
            st.info(f"Total Chapter/topics :- {get_total_subject_chapter(current_user_id,current_subject_id)}")

    with info2:
        with st.container(border=True):
            st.success(f"✅ Completed Chapter :- {get_total_copleted_subject_chapter(current_user_id,current_subject_id)}")

    with info3:
        with st.container(border=True):
            st.warning(f"🟡 Pending Chapter :- {get_total_subject_chapter(current_user_id,current_subject_id)-get_total_copleted_subject_chapter(current_user_id,current_subject_id)}")
    

    st.write("")

    # ---------- ADD SUBJECT SECTION ----------

    with st.container(border=True):

        st.subheader("➕ Add New Chapter")

        topic_name = st.text_input(
            "Chapter Name",
            placeholder="Enter chapter name"
        )

        if st.button(
            "Add chapter",
            use_container_width=True
        ):

            if topic_name.strip() == "":
                st.warning("Please enter chapter name")

            else:

                # ----- CHECK DUPLICATE TOPIC -----

                existing_topic = topics_collection.find_one({
                    "user_id": current_user["_id"],
                    "subject_id": current_subject_id,
                    "topic_name": topic_name
                })

                if existing_topic:
                    st.error("Topic already exists")

                else:

                    # ----- TOPIC DATA -----

                    topic_data = {
                        "user_id": current_user["_id"],
                        "subject_id": current_subject_id,
                        "topic_name": topic_name,
                        "completed": False
                    }

                    topics_collection.insert_one(topic_data)

                    st.success("Topic Added Successfully")

                    st.rerun()
    st.write("")


    # ---------- FETCH TOPICS ----------

    topics = list(
        topics_collection.find({
            "user_id": current_user["_id"],
            "subject_id": current_subject_id
        })
    )


    # ---------- TOPICS SECTION ----------

    st.subheader("📚 Study Chapters")

    st.write("")


    if len(topics) == 0:

        st.info("No chapters added yet")


    else:

        for index, topic in enumerate(topics, start=1):


            # ---------- TOPIC ROW CARD ----------

            with st.container(border=True):


                # ---------- TOP SECTION ----------

                top_col1, top_col2,top_col3,top_col4 = st.columns(4)

                # ----- CHAPTER INFO -----

                with top_col1:
                    st.write(
                        f"### {index}. 📖 {topic['topic_name']}"
                    )

                # ----- STATUS BADGE -----

                with top_col2:

                    if topic["completed"]:

                        st.markdown(
                            """
                            <div style="
                                background-color:#d1fae5;
                                color:#065f46;
                                padding:6px 12px;
                                border-radius:20px;
                                text-align:center;
                                font-weight:600;
                                margin-top:12px;
                            ">
                            ✅ Done
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                    else:

                        st.markdown(
                            """
                            <div style="
                                background-color:#fef3c7;
                                color:#92400e;
                                padding:6px 12px;
                                border-radius:20px;
                                text-align:center;
                                font-weight:600;
                                margin-top:12px;
                            ">
                            📌 Pending
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
                

                # ----- COMPLETE / UNDO BUTTON -----

                with top_col3:

                    # ---------- MARK COMPLETE ----------

                    if not topic["completed"]:

                        if st.button(

                            "✅ Mark Complete",

                            key=f"complete_{topic['_id']}",

                            use_container_width=True
                        ):

                            topics_collection.update_one(

                                {"_id": topic["_id"]},

                                {"$set": {"completed": True}}
                            )


                            add_activity(

                                current_user_id,

                                "Completed Topic",

                                f"Completed {topic['topic_name']}"
                            )


                            st.rerun()


                    # ---------- UNDO COMPLETE ----------

                    else:

                        if st.button(
                            "↩ Undo",
                            key=f"undo_{topic['_id']}",
                            use_container_width=True
                        ):

                            topics_collection.update_one(
                                {"_id": topic["_id"]},
                                {"$set": {"completed": False}}
                            )


                            add_activity(
                                current_user_id,
                                "Undo Topic",
                                f"Marked Pending {topic['topic_name']}"
                            )


                            st.rerun()

                with top_col4:

                    if st.button(

                        "❌ Delete",

                        key=f"delete_{topic['_id']}",

                        use_container_width=True
                    ):

                        topics_collection.delete_one({

                            "_id": topic["_id"]
                        })

                        st.rerun()


                st.write("")


                # ---------- ACTION BUTTONS ----------

                


                # ----- COMPLETE BUTTON -----

     

                    


                # ----- DELETE BUTTON -----


                    


            st.write("")

else:
    dash_col1, dash_col2 = st.columns([7, 2])

    with dash_col1:
        st.title("📗 Chapter Page")
        st.warning("Please SigIn first!!!")

    with dash_col2:
        if st.button("🔑 Sign In"):
            st.session_state.page="signin"
            st.switch_page("App.py")