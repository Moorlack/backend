from src.errors.category import UserAlreadyApproved
from src.models.category import Category
import src.repositories.category as repository
import src.repositories.user as user_repository
from src.utils.db import db


def create_category(dto):
    category = Category(
        name=dto['name']
    )

    repository.create_category(category)

    return {'id': category.id}


def delete_category(category_id):
    category = repository.get_category_by_id(category_id)
    repository.delete_category(category)


def add_approved_user(dto):
    category: Category = repository.get_category_by_id(dto['category_id'])
    is_user_exists = is_has_approved_user(category, dto['user_id'])
    if is_user_exists:
        raise UserAlreadyApproved()

    user = user_repository.get_by_id(dto['user_id'])
    category.approvedUsers.append(user)
    db.session.commit()


def is_user_approved(category: Category, user_id):
    is_public = len(category.approvedUsers) == 0

    if is_public:
        return True

    return is_has_approved_user(category, user_id)


def is_has_approved_user(category, user_id):
    return any(user.id == user_id for user in category.approvedUsers)