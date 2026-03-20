from utils import Utils
import random

class Car:
	def __init__(self, register_number):
		self._register_number = register_number
		self._max_speed = self.generate_max_speed()
		self._current_speed = 60
		self._traveled_distance = 0
	
	def accelerate(self, speed):
		self._current_speed += speed

		self._current_speed = Utils.clamp(self._current_speed, 0, self._max_speed)
	
	def travel(self, timeInHours):
		if timeInHours < 0:
			return

		self._traveled_distance += self._current_speed * timeInHours
	
	def generate_max_speed(self) -> int:
		minSpeed = 100
		maxSpeed = 200

		return random.randint(minSpeed, maxSpeed + 1)