from flask import Blueprint
from flask_restful import Api
from dependencies.createAccount import CreateAccount
from dependencies.userSignIn import UserSignIn
from dependencies.verify import Verify

apiBP = Blueprint('api', __name__)
api = Api(apiBP)

# Route
api.add_resource(CreateAccount, '/createAccount')

api.add_resource(UserSignIn, '/userSignIn')

api.add_resource(Verify, '/verify')