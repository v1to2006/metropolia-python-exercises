from car import Car
import random

class Competition:
	def __init__(self, players: list[Car]):
		self._players = players
		self._win_distance = 10000
		self._cycle_time = 1
	
	def run(self):
		while not self.has_winner():
			self.drive_cycle()
		
		self.print_winners()

	def drive_cycle(self):
		min_accelerate_speed = -10
		max_accelerate_speed = 15

		for player in self._players:
			player.accelerate(random.randint(min_accelerate_speed, max_accelerate_speed))
		
		for player in self._players:
			player.travel(self._cycle_time)
		
	def has_winner(self) -> bool:
		return any(player.traveled_distance >= self._win_distance for player in self._players)

	def print_winners(self):
		sorted_players = sorted(self._players, key=lambda player: player.traveled_distance, reverse=True)

		print("Position | Register | Max speed | Current speed | Distance")

		for i, player in enumerate(sorted_players, start=1):
			print(f"{i} | {player}")