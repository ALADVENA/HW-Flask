from flask import Flask, jsonify, request
from flask.views import MethodView



from models import User, Session


app = Flask('app')

# app.add_url_rule('')

class UserViev(MethodView):
    def get(self, user_id):
        pass
    def post(self, user_id):
        json_data = request.json
        with Session() as session:
            new_title = User (
                title = json_data['title']
                description = json_data['description']
                owner = json_data['owner']
            )
            session.add(new_title)
            session.commit()
            return new_title.json()
        
        pass
    def delete(self, user_id):
        pass

app.run()