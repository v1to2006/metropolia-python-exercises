from utils import Utils
import random

class Car:
	def __init__(self, register_number: str):
		self._register_number = register_number
		self._max_speed = self.generate_max_speed()
		self._current_speed = 60
		self._traveled_distance = 0
	
	def __str__(self):
		return f"{self._register_number} - Distance: {self._traveled_distance} - Max speed: {self._max_speed}"
	
	@property
	def register_number(self):
		return self._register_number
	
	@property
	def max_speed(self):
		return self._max_speed

	@property
	def traveled_distance(self):
		return self._traveled_distance
	
	def accelerate(self, speed : float):
		self._current_speed += speed

		self._current_speed = Utils.clamp(self._current_speed, 0, self._max_speed)
	
	def travel(self, time_in_hours : float):
		if time_in_hours < 0:
			return

		self._traveled_distance += self._current_speed * time_in_hours
	
	@staticmethod
	def generate_max_speed() -> int:
		min_speed = 100
		max_speed = 200

		return random.randint(min_speed, max_speed)