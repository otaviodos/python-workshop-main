from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID

from src.models import db


class User(db.Model):

    id = db.Column('id', UUID(as_uuid=True), default=uuid4, nullable=False, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150))
    birth_date = db.Column(db.String(10))
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, nullable=True, onupdate=datetime.now())

    def __init__(self, name, email, birth_date):
        self.name = name
        self.email = email
        self.birth_date = birth_date

    def get_as_dict(self):
        person = {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'birth_date': self.birth_date
        }
        return person
