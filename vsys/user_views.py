from pyramid.view import view_config

@view_config(route_name='users.register', renderer='json', request_method="POST")
def register(request):
    return {'success': True}