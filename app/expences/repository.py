import json

from app.expences.model import Expenses
from sqlalchemy.sql import func
from app import db
from flask import jsonify


class CatalogRepository:
    def get_all(self, args):
        expenses = Expenses.query
        if "member_name" in args.keys():
            expenses = expenses.filter_by(member_name=args.get("member_name"))
        if "department" in args.keys():
            expenses = expenses.filter_by(department=args.get("department"))
        if "amount" in args.keys():
            expenses = expenses.filter_by(amount=args.get("amount"))
        if "amount[gte]" in args.keys():
            expenses = expenses.filter(Expenses.amount >= args.get("amount[gte]"))

        expenses = expenses.all()
        return Expenses.serialize_list(expenses)

    def get_one(self, id, fields):
        expenses = Expenses.query(*(getattr(Expenses, column) for column in fields)).filter_by(id=id).first()
        return expenses.serialize()

    def sum(self, by):
        if by is not None:
            ex_sum = Expenses.query(func.sum(Expenses.amount).label("total")).groub_by(by).scalar()
        else:
            ex_sum = db.session.query(db.func.sum(Expenses.amount)).first()

        return (ex_sum)
