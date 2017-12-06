from vsys.models.vehicle import Vehicle
from vsys.models.database import MongoDatabase

from bson import ObjectId

class VehicleController(object):

	def __init__(self):
		self.db = MongoDatabase().instance()
	
	def register(self, vehicle):
		errors = self.validate(vehicle)
		if not errors:
			vehicle_to_insert = {
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
			vehicle_inserted = self.db.vehicles.insert(vehicle_to_insert)
			vehicle.id = vehicle_inserted

			if vehicle_inserted:
				vehicle_to_insert['success'] = True
				vehicle_to_insert['_id'] = str(vehicle_to_insert['_id'])
				return vehicle_to_insert

			erros['vehicle_not_iserted'] = True
		return errors

	def validate(self, vehicle):
		errors = {}
		if not vehicle.model:
			errors['empty_model'] = True
		if not vehicle.year:
			errors['empty_year'] = True
		if not vehicle.license_plate:
			errors['empty_license_plate'] = True

		return errors

	def get_vehicles(self):
		vehicles = list(self.db.vehicles.find({}))
		for vehicle in vehicles:
			vehicle['_id'] = str(vehicle.get('_id'))
		return vehicles

	def get_vehicles_by_type(self, vehicle_type):
		vehicles_by_type = list(self.db.vehicles.find({'vehicle_type': vehicle_type}))
		for vehicle in vehicles_by_type:
			vehicle['_id'] = str(vehicle.get('_id'))
		return vehicles_by_type

	def get_vehicle(self, vehicle_id):
		vehicle_id = ObjectId(vehicle_id)
		vehicle_db = self.db.vehicles.find_one({"_id": vehicle_id})
		vehicle = Vehicle(
			vehicle_db['vehicle_type'],
			vehicle_db['brand'],
			vehicle_db['model'],
			vehicle_db['year'],
			vehicle_db['category'],
			vehicle_db['color'],
			vehicle_db['license_plate'],
			vehicle_db['seats'],
			vehicle_db['num_doors'],
			vehicle_db['fuel_type'],
			vehicle_db['value'])
		vehicle.id = str(vehicle_db.get('_id'))
		return vehicle

	def edit_vehicle(self, vehicle):
		errors = self.validate(vehicle)
		if not errors:
			vehicle_json = {
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
			self.db.vehicles.update({"_id": ObjectId(vehicle.id)}, {'$set':vehicle_json})
			return vehicle_json

		return {'error': errors}

	def delete_vehicle(self, vehicle):
		self.db.vehicles.remove({"_id": ObjectId(vehicle.id)})
		return {'success': True}