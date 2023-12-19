from flask_jwt_extended import create_access_token
from passlib.handlers.pbkdf2 import pbkdf2_sha256
import src.repositories.user as user_repository
from src.errors.auth import InvalidCredentialsError


def login(dto):
    user = user_repository.find_by_name(dto['name'])

    if user is None or not pbkdf2_sha256.verify(dto['password'], user.password):
        raise InvalidCredentialsError()

    return {'access_token': create_access_token(identity=user.name)}
