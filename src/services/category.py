from src.models.category import Category
import src.repositories.category as repository


def create_category(dto):
    category = Category(
        name=dto['name']
    )

    repository.create_category(category)

    return {'id': category.id}


def delete_category(category_id):
    category = repository.get_category_by_id(category_id)
    repository.delete_category(category)
