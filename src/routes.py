from flask_restful import Api, Resource

from src.handlers.user import UsersHandler, UserHandler
from src.handlers.debit import DebitsHandler, DebitHandler, DebitUserHandler


def init_resources(app):
    api = Api()

    api.add_resource(HealthCheckHandler, "/workshop/health-check")
    api.add_resource(UsersHandler, "/workshop/users/v1")
    api.add_resource(UserHandler, "/workshop/users/v1/<id>")
    api.add_resource(DebitsHandler, "/workshop/debit/v1")
    api.add_resource(DebitHandler, "/workshop/debit/v1/<id>")
    api.add_resource(DebitUserHandler, "/workshop/debit/user/v1/<id>")

    api.init_app(app)


class HealthCheckHandler(Resource):

    @staticmethod
    def get():
        return 'ok'
