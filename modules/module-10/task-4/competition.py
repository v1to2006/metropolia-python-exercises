from car import Car
import random

class Competition:
	def __init__(self, name, distance_in_km, cars: list[Car]):
		self._name = name
		self._cars = cars
		self._distance_in_km = distance_in_km
		self._cycle_time = 1
	
	def run(self):
		while not self._has_winner():
			self._drive_cycle()
			self._print_state()
		
	def _drive_cycle(self):
		min_accelerate_speed = -10
		max_accelerate_speed = 15

		for car in self._cars:
			car.accelerate(random.randint(min_accelerate_speed, max_accelerate_speed))
		
		for car in self._cars:
			car.travel(self._cycle_time)
	
	def _print_state(self):
		sorted_cars = sorted(self._cars, key=lambda car: car.traveled_distance, reverse=True)

		print("\nPosition | Register | Max speed | Current speed | Distance")

		for i, car in enumerate(sorted_cars, start=1):
			print(f"{i} | {car}")
	
	def _has_winner(self) -> bool:
		return any(car.traveled_distance >= self._distance_in_km for car in self._cars)