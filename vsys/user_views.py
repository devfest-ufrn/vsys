from pyramid.view import view_config

from vsys.models.user import User

@view_config(route_name='users.register', renderer='json', request_method="POST")
def register(request):
    params = request.params
    _return = {}
    
    if params:
        print "oi"
    else:
        _return = {"success": False, "msg": "Missing parameters"}

    return _return