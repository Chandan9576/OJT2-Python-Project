from Databases.Connection import users_collection


def change_password(

    current_user_id,

    new_password,

    confirm_password
):

    # ---------- CHECK NEW PASSWORD MATCH ----------

    if new_password != confirm_password:

        return "Passwords do not match"


    # ---------- CHECK EMPTY PASSWORD ----------

    if new_password.strip() == "":

        return "Password cannot be empty"


    # ---------- UPDATE PASSWORD ----------

    users_collection.update_one(

        {"_id": current_user_id},

        {

            "$set": {

                "password": new_password
            }
        }
    )


    # ---------- SUCCESS ----------

    return "Password updated successfully"