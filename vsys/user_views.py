from pyramid.view import view_config

from vsys.models.user import User
from vsys.controllers.user import UserController

user_controller = UserController()
@view_config(route_name='users', request_method="POST", renderer='json')
def register(request):
    params = request.params
    _return = {}

    if params:
        first_name = params.get('first_name')
        last_name = params.get('last_name')
        email = params.get('email')
        password = params.get('password')

        user = User(first_name, last_name, email, password)

        _return = user_controller.register(user)
        
    else:
        _return = {"success": False, "msg": "Missing parameters"}

    return _return

@view_config(route_name="users", request_method="GET", renderer='json')
def list(request):
    return user_controller.get_users()

@view_config(route_name="user", request_method="GET", renderer='json')
def get_user(request):
    user_id = request.matchdict['user_id']
    user = user_controller.get_user(user_id)
    return {
        "first_name": user.first_name, 
        "last_name": user.last_name, 
        "email": user.email,
    }

@view_config(route_name="user", request_method="PUT", renderer='json')
def edit_user(request):
    user_id = request.matchdict['user_id']
    user = user_controller.get_user(user_id)

    params = request.params

    if params:
        user.first_name = params.get('first_name', user.first_name)
        user.last_name = params.get('last_name', user.last_name)
        user.email = params.get('email', user.email)
        user.password = params.get('password', user.password)

        edited_user = user_controller.edit_user(user)
        
        if not 'errors' in edited_user:
            _return = {
                "first_name": user.first_name, 
                "last_name": user.last_name, 
                "email": user.email,
            }
        else:
            _return = edited_user
        
    else:
        _return = {"success": False, "msg": "Missing parameters"}

    return _return
