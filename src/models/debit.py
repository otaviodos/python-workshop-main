from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID

from src.models import db


class Debit(db.Model):

    id = db.Column('id', UUID(as_uuid=True), default=uuid4, nullable=False, primary_key=True)
    user_id = db.Column('user_id', UUID(as_uuid=True))
    company_name = db.Column(db.String(150))
    value = db.Column(db.Numeric(10,2))
    date = db.Column(db.String(10))
    status = db.Column(db.Integer())
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, nullable=True, onupdate=datetime.now())

    def __init__(self, user_id, company_name, value, date):
        self.user_id = user_id
        self.company_name = company_name
        self.value = value
        self.date = date
        self.status = 1

    def get_as_dict(self):
        debit = {
            'id': self.id,
            'user_id': self.user_id,
            'company_name': self.company_name,
            'value': str(self.value),
            'date': self.date,
            'status': self.status
        }
        return debit
