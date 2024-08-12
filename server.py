from flask import Flask, jsonify, request
from flask.views import MethodView



from models import User, Session


app = Flask('app')


class UserViev(MethodView):
    def get(self, user_id):
        pass
    def post(self, user_id):
        json_data = request.json
        with Session() as session:
            new_advertisement = User(
                title = json_data['title']
                description = json_data['description']
                owner = json_data['owner']
            )
            session.add(new_advertisement)
            session.commit()
            return new_advertisement.json()
        
        pass
    def delete(self, user_id):
        pass

user_view = UserView.as_view('user')

app.add_url_rule( 
    rule: '/user/<int:user_id>', 
    view_func=user_view, 
    method=['GET', 'POST', 'DELETE']
    )

app.add_url_rule( 
    rule: '/user/<int:user_id>', 
    view_func=user_view, 
    method=['POST']
    )


app.run()