from src.models.user_to_category import user_to_category_table
from src.utils.db import db


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    records = db.relationship('Record', back_populates='category')
    approvedUsers = db.relationship(
        'User',
        secondary=user_to_category_table,
        back_populates='approvedCategories'
    )
