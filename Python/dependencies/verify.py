from flask_restful import Resource
from flask import request
from doqu import db, User, Task
import random
import string


class Verify(Resource):

    def post(self):
        header = request.headers["Authorization"]
        json_data = request.get_json(force=True)

        if not header:
            return ("API Key not Found"), 400
        else:
            user = User.query.filter_by(api_key=header).first()
            if user:
                verify = Verify(
                    title = json_data['title'],
                    user_id = user.id,
                    item = json_data['item'],
                )
                db.session.add(verify)
                db.session.commit()

                result = Task.serialize(verify)
                return {"status": 'success', 'data': result}, 201
            else:
                return ("No user found with that API Key"), 402

    def get(self):
        result = []
        header = request.headers["Authorization"]

        if not header:
            return ("No API Key"), 400
        else:
            user = User.query.filter_by(api_key=header).first()
            if user:
                tasks = Task.query.filter_by(user_id=user.id).all()
                for task in tasks:
                    result.append(Task.serialize(task))


            return {"status": 'success', 'data': result}, 201