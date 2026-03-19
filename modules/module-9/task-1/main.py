class Car:
	def __init__(self, register_number, max_speed):
		self.__register_number = register_number
		self.__max_speed = max_speed
		self.__current_speed = 0
		self.__traveled_distance = 0
	
	def print_info(self):
		print(f"Register number: {self.__register_number}")
		print(f"Max speed: {self.__max_speed} km/h")
		print(f"Current speed: {self.__current_speed} km/h")
		print(f"Traveled distance: {self.__traveled_distance} km")

def main():
	car = Car("ABC-123", 142)

	car.print_info()

main()