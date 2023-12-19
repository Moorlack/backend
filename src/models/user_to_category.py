from src.utils.db import db, Base

user_to_category_table = db.Table(
    'user_to_category',
    Base.metadata,
    db.Column('user_id', db.ForeignKey('users.id'), primary_key=True),
    db.Column('category_id', db.ForeignKey('categories.id'), primary_key=True)
)