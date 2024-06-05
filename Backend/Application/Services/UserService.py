
from optionsinsight.Backend.Domain.Entities.Users import UserModel, db

def register_user(username, email, password):
    if UserModel.find_by_username(username):
        raise ValueError("Username already exists")

    new_user = UserModel(username=username, email=email)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def authenticate_user(username, password):
    user = UserModel.find_by_username(username)
    if user and user.check_password(password):
        return user
    return None
