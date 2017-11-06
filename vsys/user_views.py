from pyramid.view import view_config

from vsys.models.user import User
from vsys.controllers.user import UserController

@view_config(route_name='users.register', renderer='json', request_method="POST")
def register(request):
    params = request.params
    _return = {}

    if params:
        first_name = params.get('first_name')
        last_name = params.get('last_name')
        email = params.get('email')
        password = params.get('password')

        user = User(first_name, last_name, email, password)
        user_controller = UserController()
        _return = user_controller.register(user)
        
    else:
        _return = {"success": False, "msg": "Missing parameters"}

    return _return