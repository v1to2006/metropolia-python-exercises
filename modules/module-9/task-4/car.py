from utils import Utils
import random

class Car:
	def __init__(self, register_number):
		self.__register_number = register_number
		self.__max_speed = self.generate_max_speed()
		self.__current_speed = 60
		self.__traveled_distance = 0
	
	def accelerate(self, speed):
		self.__current_speed += speed

		self.__current_speed = Utils.clamp(self.__current_speed, 0, self.__max_speed)
	
	def travel(self, timeInHours):
		if timeInHours < 0:
			return

		self.__traveled_distance += self.__current_speed * timeInHours
	
	def generate_max_speed(self) -> int:
		minSpeed = 100
		maxSpeed = 200

		return random.randint(minSpeed, maxSpeed + 1)