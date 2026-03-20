class Car:
	def __init__(self, register_number, max_speed):
		self._register_number = register_number
		self._max_speed = max_speed
		self._current_speed = 0
		self._traveled_distance = 0
	
	def print_info(self):
		print(f"Register number: {self._register_number}")
		print(f"Max speed: {self._max_speed} km/h")
		print(f"Current speed: {self._current_speed} km/h")
		print(f"Traveled distance: {self._traveled_distance} km")

def main():
	car = Car("ABC-123", 142)

	car.print_info()

main()