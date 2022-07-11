from app import db
from datetime import datetime
from app.expences.serialize import Serializer


class Expenses(db.Model, Serializer):
    __tablename__ = 'expenses'

    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(50), nullable=False, index=True)
    project_name = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float)
    date = db.Column(db.DateTime, default=datetime.utcnow())
    member_name = db.Column(db.String(100), nullable=False)

    def __int__(self, department, project_name, amount, date, member_name):
        self.department = department
        self.project_name = project_name
        self.amount = amount
        self.date = date
        self.member_name = member_name

    def serialize(self):
        return Serializer.serialize(self)
