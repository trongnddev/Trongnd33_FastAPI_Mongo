import re


def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "fullname": user["fullname"],
        "email": user["email"],
        "course_of_study": user["course_of_study"],
        "year": user["year"],
        "GPA": user["gpa"],
    }


def users_helper(users) -> list:
    return [user_helper for user in users]