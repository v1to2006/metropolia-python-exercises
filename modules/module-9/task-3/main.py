def clamp(current, min, max) -> int:
	if current > max:
		return max
	elif current < min:
		return min
	else:
		return current

class Car:
	def __init__(self, register_number, max_speed):
		self.__register_number = register_number
		self.__max_speed = max_speed
		self.__current_speed = 60
		self.__traveled_distance = 0
	
	def accelerate(self, speed):
		self.__current_speed += speed

		self.__current_speed = clamp(self.__current_speed, 0, self.__max_speed)
	
	def travel(self, timeInHours):
		if timeInHours < 0:
			return

		self.__traveled_distance += self.__current_speed * timeInHours
	
	def print_info(self):
		print(f"Register number: {self.__register_number}")
		print(f"Max speed: {self.__max_speed} km/h")
		print(f"Current speed: {self.__current_speed} km/h")
		print(f"Traveled distance: {self.__traveled_distance} km")

def main():
	car = Car("ZOV-432", 200)

	while (True):
		car.print_info()
		car.travel(float(input("Enter travel time (h): ")))

main()