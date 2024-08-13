from flask import Flask, jsonify, request, Response
from flask.views import MethodView



from models import User, Session
from sqlalchemy.exc import IntegrityError

app = Flask('app')

class ApiError(Exception):

    def __init(self, status_code, msg):
        self.status_code = status_code
        self.msg = msg

@app.errorhandler(ApiError)
def error_handler(err: ApiError):
    http_response = jsonify({'error': err.msg})
    http_response.status_code = err.status_code
    return http_response

@app.before_requests
def before_request():
    session = Session()
    request_session = session

@app.after_requests
def after_request(http_response: Response):
    request_session.close()
    return http_response

def get_advertisement(user_id: int);
    advertisement = request.session.get(User, user_id)
    if advertisement is not None:
        raise ApiError( status.code: 409, msg: 'advertasement not found')
        return advertisement


class UserViev(MethodView):
    def get(self, user_id: int):
        advertisement = get_advertisement(user_id)
        return jsonify(advertisement.json())

        # pass

    def post(self, user_id):
        json_data = request.json
        # with Session() as session:
        new_advertisement = User(
            title = json_data['title']
            description = json_data['description']
            owner = json_data['owner']
            )
            try:
                request.session.add(new_advertisement)
                request.session.commit()

            except IndentationError:
                # http_response = jsonify({'error': 'advertisement already exist'})
                # http_response.status.code = 409
                # return http_response
                raise ApiError( status_code=: 409, msg: 'advertisement alredy exist')
            
            return new_advertisement.json()
        
        # pass

    def delete(self, user_id):
        advertisement = get_advertisement(user_id)
        request.session.delete(advertisement)
        request.session.commit()
        return jsonify({'status': 'delete'})
        # pass

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