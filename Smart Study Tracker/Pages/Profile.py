import streamlit as st
from Auth.Signin import show_signin
from Utils.Session_State import logout
from Utils.Session_State import navigate
from Components.PageConfig import show_PageConfig,show_logo
from Utils.Avtivity import add_activity
from Utils.Avtivity import get_recent_activity
from Utils.Analytics import get_total_completed_chapter
from Utils.Analytics import get_total_chapter
from Utils.Analytics import get_total_subject
from Utils.Analytics import get_total_subject_chapter
from Utils.Analytics import get_total_copleted_subject_chapter
from Utils.Analytics import get_total_completed_subjects
from Databases.Connection import users_collection
from Databases.Connection import subjects_collection
from Databases.Connection import topics_collection
from Databases.Connection import activity_logs_collection
import time


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

        current_user = st.session_state.current_user

        st.title(f"👤 Welcome, {st.session_state.current_user['username']}")
            
    
    # ---------- PROFILE TOP SECTION ----------

    profile_col1, profile_col2 = st.columns([1, 3])


    # ---------- PROFILE IMAGE ----------

    with profile_col1:

            st.markdown(
                """
                <div style="
                    width:140px;
                    height:140px;
                    border-radius:50%;
                    background:#1f2937;
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    font-size:50px;
                    color:white;
                    margin:auto;
                ">
                👤
                </div>
                """,
                unsafe_allow_html=True
            )


    # ---------- USER INFO ----------

    with profile_col2:

        st.write(f"#### Name : {current_user['full_name']}")

        st.write(f"📧 Email : {current_user['email']}")

        st.write(f"👤 Username : {current_user["username"]}")

        st.write(f"🔏 Current Password : {current_user["password"]}")

    st.divider()


    # ---------- QUICK STATS ----------

    st.subheader("📊 Study Overview")

    stats_col1, stats_col2, stats_col3, stats_col4 = st.columns(4)


    with stats_col1:

        with st.container(border=True):
            st.metric("📘 Total Subjects",get_total_subject(current_user["_id"]))


    with stats_col2:

        with st.container(border=True):
            st.metric("📖 Total Chapter",get_total_chapter(current_user["_id"]))

    with stats_col3:
        with st.container(border=True):
            st.metric("📘 Completed Subject",get_total_completed_subjects(current_user["_id"],))


    with stats_col4:

        with st.container(border=True):
            st.metric("✅ Completed Chapter",get_total_completed_chapter(current_user["_id"]))

    st.write("")


    with st.container(border=True):

            if get_total_chapter(current_user["_id"]) > 0:
                progress_percentage = (get_total_completed_chapter(current_user["_id"]) / get_total_chapter(current_user["_id"])) * 100
                st.info(f"Overall profress: {progress_percentage:.2f} %")
                st.progress(progress_percentage / 100)
            else:
                st.write("0")


    st.write("")
    st.divider()


    # ---------- ACCOUNT SECTION ----------

    st.subheader("⚙ Account Settings")


    with st.container(border=True):

        st.write("### 🖋️ Edit Profile")

        new_name = st.text_input("Update Name",value=current_user["full_name"])
        new_username = st.text_input("Update UserName",value=current_user["username"])
        new_email = st.text_input("Update Email",value=current_user["email"], disabled=True)
        new_password = st.text_input("Update Password",value=current_user["password"], disabled=True)


        st.write("")

        if st.button("Save Changes",use_container_width=True):
            if (new_name.strip() == ""or new_username.strip() == ""):

                st.error(

                    "Fields cannot be empty")


            # ---------- CHECK USERNAME DUPLICATE ----------

            else:

                existing_username = users_collection.find_one({

                    "username": new_username,

                    "_id": {

                        "$ne": current_user["_id"]
                    }
                })


                # ---------- USERNAME EXISTS ----------

                if existing_username:

                    st.error("Username already taken")


                # ---------- UPDATE PROFILE ----------

                else:

                    users_collection.update_one(

                        {

                            "_id": current_user["_id"]
                        },

                        {

                            "$set": {

                                "full_name": new_name,

                                "username": new_username
                            }
                        }
                    )


                    # ---------- UPDATE SESSION ----------

                    st.session_state.current_user["full_name"] = new_name

                    st.session_state.current_user["username"] = new_username


                    st.success("Profile updated successfully")
                    st.rerun()
                    

        
        st.write("")


    # ---------- ACCOUNT ACTIONS ----------

    action_col1, action_col2 = st.columns(2)

        # ---------- LOGOUT ----------

    with action_col1:

            if st.button("🚪 Logout",use_container_width=True):
                logout()
            


        # ---------- DELETE ACCOUNT ----------

    with action_col2:

            if st.button("⚠️ Delete Account",use_container_width=True):
                st.session_state.show_delete_warning = True
            

            if st.session_state.get("show_delete_warning", False):

                st.error("⚠️ This action will permanently delete your account and all study data.")

                confirm_delete = st.checkbox("I understand this action cannot be undone")


                if confirm_delete:

                    if st.button("❌ Permanently Delete My Account",use_container_width=True):

                        users_collection.delete_one({
                            "_id": st.session_state.current_user["_id"]
                        })

                        subjects_collection.delete_many({

                            "user_id": st.session_state.current_user["_id"]
                        })

                        topics_collection.delete_many({

                            "user_id": st.session_state.current_user["_id"]
                        })

                        activity_logs_collection.delete_many({

                            "user_id": st.session_state.current_user["_id"]
                        })

                        logout()


    st.write("")
    st.divider()


    # ---------- RECENT ACTIVITY ----------

    st.subheader("📌 Recent Activity")

    recent_activities = get_recent_activity(current_user["_id"])

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


    st.write("")


        # ---------- FOOTER ----------

    st.markdown(
            """
            <h5 style='text-align:center;color:gray;'>
            Keep learning consistently 🚀
            </h5>
            """,
            unsafe_allow_html=True
        )

    

else:
    dash_col1, dash_col2 = st.columns([7, 2])

    with dash_col1:
        st.title("👤 No Profile")
        st.warning("Please SigIn first!!!")
        st.write("")


    with dash_col2:
        if st.button("🔑 Sign In"):
            st.session_state.page="signin"
            st.switch_page("App.py")