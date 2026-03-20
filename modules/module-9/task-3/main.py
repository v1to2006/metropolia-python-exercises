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
	
	def travel(self, timeInHours):
		if timeInHours < 0:
			return

		self._traveled_distance += self._current_speed * timeInHours
	
	def print_info(self):
		print(f"Register number: {self._register_number}")
		print(f"Max speed: {self._max_speed} km/h")
		print(f"Current speed: {self._current_speed} km/h")
		print(f"Traveled distance: {self._traveled_distance} km")

def main():
	car = Car("ZOV-432", 60)

	while (True):
		car.print_info()
		car.travel(float(input("Enter travel time (h): ")))

main()