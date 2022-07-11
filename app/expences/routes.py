from flask import jsonify, request
from app.expences import main
from app.expences.service import CatalogService
from flask_parameter_validation import ValidateParameters, Query


@main.route('/expenses', methods=['GET'])
def index():
    args = request.args
    catalog = CatalogService()
    return jsonify({'expences': catalog.get_all(args)}), 201


@main.route('/expenses/<id>', methods=['GET'])
def latest(id):
    args = request.args
    fields = args.get('fields').split(",")
    catalog = CatalogService()
    return jsonify({'expences': catalog.get_one(id, fields)}), 201


@main.route('/aggregates', methods=['GET'])
def aggregates():
    args = request.args
    by = args.get('by')
    catalog = CatalogService()
    return jsonify({'aggregates': catalog.sum(by)}), 200

