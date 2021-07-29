from src.models import db
from flask import request, jsonify
from flask_restful import Resource

from src.models.user import User


class UsersHandler(Resource):

    def get(self):
        users = User.query.all()
        if not users:
            return jsonify(error='Nenhum usuario foi encontrado!')

        result = [user.get_as_dict() for user in users]

        return jsonify(result)

    def post(self):

        params = {
            'name': request.json['name'],
            'email': request.json['email'],
            'birth_date': request.json['birth_date']
        }

        user = User(**params)
        db.session.add(user)
        db.session.commit()

        return jsonify(sucess='Usuario cadastrado com sucesso!')


class UserHandler(Resource):

    def get(self, id):
        user = User.query.get(id)
        if not user:
            return jsonify(error='Usuario nao encontrado!')

        return jsonify(user.get_as_dict())

    def put(self, id):
        user = User.query.get(id)
        if not user:
            return jsonify(error='Usuario nao encontrado!')

        user.name = request.json['name']
        user.email = request.json['email']
        user.birth_date = request.json['birth_date']

        db.session.commit()

        return jsonify(sucess='Usuario atualizado com sucesso!')

    def delete(self, id):
        user = User.query.get(id)
        if not user:
            return jsonify(error='Usuario nao encontrado!')

        db.session.delete(user)
        db.session.commit()

        return jsonify(sucess='Usuario deletado com sucesso!')
