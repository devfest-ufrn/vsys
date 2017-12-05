from pyramid.config import Configurator

try:
    # for python 2
    from urlparse import urlparse
except ImportError:
    # for python 3
    from urllib.parse import urlparse

from gridfs import GridFS
from pymongo import MongoClient    

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    

    # Mongo configurations
    db_url = urlparse(settings['mongo_uri'])
    config.registry.db = MongoClient(
        host=db_url.hostname,
        port=db_url.port,
    )

    def add_db(request):
        db = config.registry.db[db_url.path[1:]]
        if db_url.username and db_url.password:
            db.authenticate(db_url.username, db_url.password)
        return db

    def add_fs(request):
        return GridFS(request.db)

    config.add_request_method(add_db, 'db', reify=True)
    config.add_request_method(add_fs, 'fs', reify=True)

    # Routes (maybe put in routes.py later)
    config.add_route('index', '/')
    config.add_route('signup', '/signup')
    config.add_route('login', '/login')

    config.add_route('rentacar', '/rentacar')
    
    config.add_route('offercar', '/offercar')
    config.add_route('register_vehicle', '/offercar/register_vehicle')

    ### Users routes:
    config.add_route('users', '/users')
    config.add_route('user', '/users/{user_id}')

    ### Vehicles routes:
    config.add_route('vehicles', '/vehicles')
    config.add_route('vehicle', '/vehicles/{vehicle_id}')
    config.add_route('vehicle_by_type', '/vehicles/type/{vehicle_type}')

    # config.scan('routes.py')
    config.scan()
    return config.make_wsgi_app()
