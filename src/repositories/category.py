from src.errors.category import CategoryNotFound
from src.models.category import Category
from src.utils.db import db


def create_category(category: Category):
    db.session.add(category)
    db.session.commit()


def delete_category(category: Category):
    db.session.delete(category)
    db.session.commit()


def get_category_by_id(category_id: int):
    category = Category.query.get(category_id)

    if category is None:
        raise CategoryNotFound(category_id)

    return category
