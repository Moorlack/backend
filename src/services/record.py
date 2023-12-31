import src.repositories.record as repository
import src.repositories.user as user_repository
import src.repositories.category as category_repository
import src.services.category as category_service
from src.errors.record import UserNotApprovedForCategory
from src.models.record import Record


def create_record(dto):
    user = user_repository.get_by_id(dto['user_id'])
    category = category_repository.get_category_by_id(dto['category_id'])

    if not category_service.is_user_approved(category, user.id):
        raise UserNotApprovedForCategory()

    record = Record(
        user_id=user.id,
        category_id=category.id,
        sum=dto['sum']
    )

    repository.create_record(record)

    return {'id': record.id}


def delete_record_by_id(record_id):
    record = repository.get_record_by_id(record_id)
    repository.delete_record(record)

    return {'success': True}
