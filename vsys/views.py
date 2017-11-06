from pyramid.view import view_config

@view_config(route_name='index', renderer='templates/index.jinja2')
def index(request):
    return {"success": True}

@view_config(route_name='rentacar', renderer='templates/rentacar.jinja2')
def rentacar(request):
    return {'success': True}

@view_config(route_name='offercar', renderer='templates/offercar.jinja2')
def offercar(request):
    return {'success': True}

@view_config(route_name='signup', renderer='templates/signup.jinja2')
def signup(request):
    return {'success': True}