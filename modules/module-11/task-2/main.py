def clamp(current, min, max) -> int:
	if current > max:
		return max
	elif current < min:
		return min
	else:
		return current

class Car:
	def __init__(self, register_number, max_speed):
		self._register_number = register_number
		self._max_speed = max_speed
		self._current_speed = max_speed
		self._traveled_distance = 0
	
	def accelerate(self, speed):
		self._current_speed += speed

		self._current_speed = clamp(self._current_speed, 0, self._max_speed)
	
	def travel(self, time_in_hours):
		if time_in_hours < 0:
			return

		self._traveled_distance += self._current_speed * time_in_hours
	
	def print_info(self):
		print(f"Register number: {self._register_number}")
		print(f"Max speed: {self._max_speed} km/h")
		print(f"Current speed: {self._current_speed} km/h")
		print(f"Traveled distance: {self._traveled_distance} km")

class ElectricCar(Car):
	def __init__(self, register_number, max_speed, battery_capacity_kwh) -> None:
		super().__init__(register_number, max_speed)
		self._battery_capacity_kwh = battery_capacity_kwh

class FuelCar(Car):
	def __init__(self, register_number, max_speed, fuel_tank_capacity_liters) -> None:
		super().__init__(register_number, max_speed)
		self._fuel_tank_capacity_liters = fuel_tank_capacity_liters

def main():
	electricCar = ElectricCar("ABC-15", 180, 52.5)
	fuelCar = FuelCar("ACD-123", 165, 32.3)

	electricCar.travel(3)
	fuelCar.travel(3)

	electricCar.print_info()
	print()
	fuelCar.print_info()

main()