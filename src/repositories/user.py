from typing import List
from src.errors.user import UserNotFoundError
from src.models.user import User
from src.utils.db import db


def create_user(user: User):
    db.session.add(user)
    db.session.commit()


def delete_user(user: User):
    db.session.delete(user)
    db.session.commit()


def get_by_id(user_id):
    user = User.query.get(user_id)

    if user is None:
        raise UserNotFoundError()

    return user


def get_all_users() -> List[User]:
    return User.query.all()


def is_exists_with_name(name):
    return find_by_name(name) is not None


def find_by_name(name):
    return User.query.filter(User.name == name).first()
