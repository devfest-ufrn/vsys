from pyramid.view import view_config
from vsys.controllers.vehicle import VehicleController

vehicle_controller = VehicleController()

@view_config(route_name='index', renderer='templates/index.jinja2')
def index(request):
    return {"success": True}

@view_config(route_name='rentacar', renderer='templates/rentacar.jinja2')
def rentacar(request):
    vehicles = vehicle_controller.get_vehicles()

    cars = []
    motos = []
    bikes = []

    for vehicle in vehicles:
        if vehicle['vehicle_type'] == "Car":
            cars.append(vehicle)
        elif vehicle['vehicle_type'] == "Motorcycle":
            motos.append(vehicle)
        else:
            bikes.append(vehicle)

    return {'cars': cars, 'motos': motos, 'bikes': bikes}

@view_config(route_name='offercar', renderer='templates/offercar.jinja2')
def offercar(request):
    return {'success': True, 'vehicles': vehicle_controller.get_vehicles()}

@view_config(route_name='signup', renderer='templates/signup.jinja2')
def signup(request):
    return {'success': True}

@view_config(route_name='register_vehicle', renderer='templates/register_vehicle.jinja2')
def register_vehicle(request):
    return {'success': True}

@view_config(route_name='login', renderer='templates/login.jinja2')
def login(request):
    return {'success': True}

@view_config(route_name='vehicle_show', renderer='templates/vehicle.jinja2')
def vehicle(request):
    vehicle_id = request.matchdict['vehicle_id']
    vehicle = vehicle_controller.get_vehicle(vehicle_id)
    return {
                'vehicle_type' : vehicle.vehicle_type,
                'brand': vehicle.brand,
                'model': vehicle.model,
                'year': vehicle.year,
                'category': vehicle.category,
                'color': vehicle.color,
                'license_plate': vehicle.license_plate,
                'seats': vehicle.seats,
                'num_doors': vehicle.num_doors,
                'fuel_type' : vehicle.fuel_type,
                'value' : vehicle.value
            }