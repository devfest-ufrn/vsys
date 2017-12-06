class Vehicle():

	def __init__(self, vehicle_type, category, brand, model, year, color, license_plate, seats, num_doors, fuel_type, value):
		self._vehicle_type = vehicle_type #1 = car, 2 = motorcycle, 3 = bike 
		self._category = category 
		self._brand = brand
		self._model = model
		self._year = year
		self._color = color
		self._license_plate = license_plate
		self._seats = seats
		self._num_doors = num_doors
		self._fuel_type = fuel_type
		self._value = value
		self._id = None

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, value):
		self._id = value

	@property
	def vehicle_type(self):
		return self._vehicle_type

	@vehicle_type.setter
	def vehicle_type(self, value):
		self._vehicle_type = value

	@property
	def brand(self):
		return self._brand

	@brand.setter
	def brand(self, value):
		self._brand = value

	@property
	def model(self):
		return self._model

	@model.setter
	def model(self, value):
		self._model = value

	@property
	def year(self):
		return self._year

	@year.setter
	def year(self, value):
		self._year = value

	@property
	def category(self):
		return self._category

	@category.setter
	def category(self, value):
		self._category = value

	@property
	def color(self):
		return self._color

	@color.setter
	def color(self, value):
		self._color = value

	@property
	def license_plate(self):
		return self._license_plate

	@license_plate.setter
	def license_plate(self, value):
		self._license_plate = valulicense_plate

	@property
	def seats(self):
		return self._seats

	@seats.setter
	def seats(self, value):
		self._seats = value

	@property
	def num_doors(self):
		return self._num_doors

	@num_doors.setter
	def num_doors(self, value):
		self._num_doors = value

	@property
	def fuel_type(self):
		return self._fuel_type

	@fuel_type.setter
	def fuel_type(self, value):
		self._fuel_type = value

	@property
	def value(self):
		return self._value

	@value.setter
	def value(self, value):
		self._value = value