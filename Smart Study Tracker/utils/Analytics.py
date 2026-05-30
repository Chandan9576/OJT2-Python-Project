import streamlit as st
from databases.Connection import topics_collection
from databases.Connection import subjects_collection


def get_total_chapter(current_user_id):
    total_topics = topics_collection.count_documents({
    "user_id":current_user_id
    })
    return total_topics
    
def get_total_completed_chapter(current_user_id):
    total_completed_topics = topics_collection.count_documents({
        "user_id":current_user_id,
        "completed":True
    })
    return total_completed_topics
    
def get_total_subject(current_user_id):
    total_subject = subjects_collection.count_documents({
        "user_id":current_user_id
    })
    return total_subject

def get_total_subject_chapter(current_user_id,current_subject_id):
    total_subject_topics = topics_collection.count_documents({
        "user_id": current_user_id,
        "subject_id": current_subject_id
    })
    return total_subject_topics

def get_total_copleted_subject_chapter(current_user_id,current_subject_id):
    total_completed_subject_topics = topics_collection.count_documents({
        "user_id": current_user_id,
        "subject_id": current_subject_id,
        "completed": True
    })
    return total_completed_subject_topics

def get_total_completed_subjects(current_user_id):

    subjects = list(
        subjects_collection.find({
            "user_id": current_user_id
        })
    )

    completed_subjects = 0

    for subject in subjects:

        # ----- TOTAL TOPICS -----

        total_topics = topics_collection.count_documents({
            "user_id": current_user_id,
            "subject_id": subject["_id"]
        })


        # ----- COMPLETED TOPICS -----

        completed_topics = topics_collection.count_documents({
            "user_id": current_user_id,
            "subject_id": subject["_id"],
            "completed": True
        })


        # ----- SUBJECT COMPLETION CHECK -----

        if (total_topics > 0 and total_topics == completed_topics):
            completed_subjects += 1


    return completed_subjects

def get_subject_wise_progress(current_user_id):

    subjects = list(

        subjects_collection.find({
            "user_id": current_user_id
        })
    )


    progress_data = []


    for subject in subjects:

        # ----- TOTAL TOPICS -----

        total_subject_topics = topics_collection.count_documents({
            "user_id": current_user_id,
            "subject_id": subject["_id"]
        })


        # ----- COMPLETED TOPICS -----

        completed_subject_topics = topics_collection.count_documents({

            "user_id": current_user_id,

            "subject_id": subject["_id"],

            "completed": True
        })


        # ----- PROGRESS PERCENTAGE -----

        if total_subject_topics > 0:

            subject_progress = (
                completed_subject_topics / total_subject_topics
            ) * 100

        else:
            subject_progress = 0


        # ----- STORE DATA -----

        progress_data.append({
            "subject_name": subject["subject_name"],
            "completed_topics": completed_subject_topics,
            "total_topics": total_subject_topics,
            "progress_percentage": subject_progress
        })

    return progress_data