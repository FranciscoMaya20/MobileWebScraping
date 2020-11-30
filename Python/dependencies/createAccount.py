from flask_restful import Resource
from flask import request
from doqu import db, User
import random
import string

class CreateAccount(Resource):
    def get(self):
        users = User.query.all()
        usersList = []
        for i in range(0, len(users)):
            usersList.append(users[i].serialize())
        return { "status" : str(usersList)}, 200

    def post(self):
        json_data = request.get_json(force=True)

        if not json_data:
               return ("No Data Received"), 400

        user = User.query.filter_by(username=json_data['username']).first()
        if user:
            return ("Username not found"), 400

        user = User.query.filter_by(emailAddress=json_data['emailadress']).first()
        if user:
            return ("Email is taken"), 400
        
        api_key = self.generate_key()

        user = User.query.filter_by(api_key=api_key).first()
        if user:
            return ("API key is taken"), 400

        user = User(
            api_key = api_key,
            firstname = json_data['firstname'],
            lastname = json_data['lastname'],
            emailadress = json_data['emailadress'],
            password = json_data['password'],
            username = json_data['username'],
        )
        db.session.add(user)
        db.session.commit()

        result = User.serialize(user)

        return { "status": 'success', 'data': result }, 201

    def generateKey(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(50))
