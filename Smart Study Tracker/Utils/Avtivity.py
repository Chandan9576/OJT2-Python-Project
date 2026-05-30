from datetime import datetime

from databases.Connection import activity_logs_collection


def add_activity(current_user_id,action,message):

    activity_data = {

        "user_id": current_user_id,
        "action": action,
        "message": message,
        "created_at": datetime.now()
    }

    activity_logs_collection.insert_one(
        activity_data
    )

def get_recent_activity(current_user_id):
    recent_activities = list(

        activity_logs_collection.find({

            "user_id": current_user_id
        })

        .sort("created_at", -1)

        .limit(2)
    )


    return recent_activities