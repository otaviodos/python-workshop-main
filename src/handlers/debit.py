from src.models import db
from flask import request, jsonify
from flask_restful import Resource

from src.models.debit import Debit
from src.models.user import User


class DebitsHandler(Resource):

    def get(self):
        debits = Debit.query.all()
        if not debits:
            return jsonify(error='Nenhum debito foi encontrado!')

        result = [debit.get_as_dict() for debit in debits]

        return jsonify(result)

    def post(self):

        if not request.json.get('user_id'):
            return jsonify(error='Nenhum usuario foi informado!')
        params = {
            'user_id': request.json['user_id'],
            'company_name': request.json['company_name'],
            'value': request.json['value'],
            'date': request.json['date'],
        }

        debit = Debit(**params)
        db.session.add(debit)
        db.session.commit()

        return jsonify(sucess='Debito cadastrado com sucesso!')


class DebitHandler(Resource):

    def get(self, id):
        debit = Debit.query.get(id)
        if not debit:
            return jsonify(error='Debito nao encontrado!')

        return jsonify(debit.get_as_dict())

    def put(self, id):
        debit = Debit.query.get(id)
        if not debit:
            return jsonify(error='Debito nao encontrado!')

        if user_id:= request.json.get('user_id'):
            debit.user_id=user_id
        debit.company_name = request.json['company_name']
        debit.value = request.json['value']
        debit.date = request.json['date']
        debit.status = request.json['status']

        db.session.commit()

        return jsonify(sucess='Debito atualizado com sucesso!')

    def delete(self, id):
        debit = Debit.query.get(id)
        if not debit:
            return jsonify(error='Debito nao encontrado!')

        db.session.delete(debit)
        db.session.commit()

        return jsonify(sucess='Debito deletado com sucesso!')


class DebitUserHandler(Resource):

    def get(self, id):
        debits = Debit.query.filter(Debit.user_id == id).all()
        if not debits:
            return jsonify(error='Debito nao encontrado!')

        result = [debit.get_as_dict() for debit in debits]

        return jsonify(result)
