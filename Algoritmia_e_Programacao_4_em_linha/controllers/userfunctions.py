import models.user as us


def submit_login(username, password, user_list):
    for i in user_list:
        if i.get_username() == username and i.get_password() != password:
            return "Incorrect Password"
        elif i.get_username() == username and i.get_password() == password:
            return i
    return "User not found"


def submit_register(username, password, password_repeat, user_list):
    for i in user_list:
        if i.get_username == username:
            return "User already exists"
    if password != password_repeat:
        return "Passwords do not match"
    else:
        user = us.User()
        user.set_username(username)
        user.set_password(password)
        return user
