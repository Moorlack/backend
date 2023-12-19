from src.utils.db import db
from src.models.user_to_category import user_to_category_table


class User (db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    records = db.relationship('Record', back_populates='user')
    approvedCategories = db.relationship(
        'Category',
        secondary=user_to_category_table,
        back_populates='approvedUsers'
    )
