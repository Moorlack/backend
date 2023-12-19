from src.errors.record import RecordNotFound
from src.models.record import Record
from src.utils.db import db


def create_record(record: Record):
    db.session.add(record)
    db.session.commit()


def get_record_by_id(record_id: int):
    record = Record.query.get(record_id)

    if record is None:
        raise RecordNotFound()

    return record


def get_records_by_filter(dto):
    query = db.session.query(Record)

    if 'user_id' in dto:
        query = query.filter_by(user_id=dto['user_id'])

    if 'category_id' in dto:
        query = query.filter_by(category_id=dto['category_id'])

    return query.all()


def delete_record(record: Record):
    db.session.delete(record)
    db.session.commit()

