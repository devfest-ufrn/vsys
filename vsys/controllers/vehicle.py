from vsys.models.database import MongoDatabase

class VehicleController(object):
	
	def __init__(self):
		self.db = MongoDatabase().instance()
	
	def register(self, vehicle):
		errors = self.vaulidate(vehicle)
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
		if not vehicle.model:
			errors['empty_model'] = True
		if not vehicle.year:
			errors['empty_year'] = True
		if not vehicle.license_plate:
			errors['empty_license_plate'] = True
		return errors