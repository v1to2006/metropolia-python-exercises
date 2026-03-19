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
		self.__current_speed = 0
		self.__traveled_distance = 0
	
	def accelerate(self, speed):
		self.__current_speed += speed

		self.__current_speed = clamp(self.__current_speed, 0, self.__max_speed)
	
	def print_current_speed(self):
		print(f"Car's current speed: {self.__current_speed} km/h")

def main():
	car = Car("ZOV-432", 200)

	while (True):
		car.print_current_speed()
		car.accelerate(int(input("Increase/Decrease speed by (km/h): ")))

main()