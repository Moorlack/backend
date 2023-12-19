from passlib.handlers.pbkdf2 import pbkdf2_sha256

from src.errors.user import UserAlreadyExistsError
from src.models.user import User
import src.repositories.user as repository


def create_user(dto):
    if repository.is_exists_with_name(dto['name']):
        raise UserAlreadyExistsError()

    user = User(
        name=dto['name'],
        password=pbkdf2_sha256.hash(dto['password'])
    )
    repository.create_user(user)

    return {"id": user.id}


def delete_user_by_id(user_id):
    user = repository.get_by_id(user_id)
    repository.delete_user(user)
