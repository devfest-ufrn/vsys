from pyramid.view import view_config

from vsys.models.vehicle import Vehicle
from vsys.controllers.vehicle import VehicleController

vehicle_controller = VehicleController()

@view_config(route_name='vehicles', request_method="POST", renderer='json')
def register(request):
	params = request.params
	_return = {}
	if params:
		vehicle_type = params.get('type')
		brand = params.get('brand')
		model = params.get('model')
		year = params.get('year')
		category = params.get('category')
		color = params.get('color')
		license_plate = params.get('license_plate')
		seats = params.get('seats')
		num_doors = params.get('num_doors')
		fuel_type = params.get('fuel')
		value = params.get('value')
		vehicle = Vehicle(  vehicle_type,
							brand,
							model,
							year,
							category,
							color,
							license_plate,
							seats,
							num_doors,
							fuel_type,
							value)
		_return = vehicle_controller.register(vehicle)

	else:
		_return = {"success": False, "msg": "Missing parameters"}

	return _return

@view_config(route_name="vehicles", request_method="GET", renderer='json')
def list(request):
	return vehicle_controller.get_vehicles()

@view_config(route_name="vehicle_by_type", request_method="GET", renderer='json')
def list_by_type(request):
	vehicle_type = request.matchdict['vehicle_type']
	return vehicle_controller.get_vehicles_by_type(vehicle_type)

@view_config(route_name="vehicle", request_method="GET", renderer='json')
def get_vehicle(request):
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


@view_config(route_name="vehicle", request_method="PUT", renderer='json')
def edit_vehicle(request):
	vehicle_id = request.matchdict['vehicle_id']
	vehicle = vehicle_controller.get_vehicle(vehicle_id)

	params = request.params

	if params:
		vehicle_type = params.get('vehicle_type', vehicle.vehicle_type)
		brand = params.get('brand', vehicle.brand)
		model = params.get('model', vehicle.model)
		year = params.get('year', vehicle.year)
		category = params.get('category', vehicle.category)
		color = params.get('color', vehicle.color)
		license_plate = params.get('license_plate', vehicle.license_plate)
		seats = params.get('seats', vehicle.seats)
		num_doors = params.get('num_doors', vehicle.num_doors)
		fuel_type = params.get('fuel_type', vehicle.fuel_type)
		value = params.get('value', vehicle.value)

		edited_vehicle = vehicle_controller.edit_vehicle(vehicle)

		if not 'errors' in edited_vehicle:
			_return = {
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
		else:
			_return = edited_vehicle
	else:
		_return = {"success": False, "msg": "Missing parameters"}

	return _return

@view_config(route_name="vehicle", request_method="DELETE", renderer='json')
def remove_vehicle(request):
	vehicle_id = request.matchdict['vehicle_id']
	vehicle = vehicle_controller.get_vehicle(vehicle_id)

	return vehicle_controller.delete_vehicle(vehicle_id)
