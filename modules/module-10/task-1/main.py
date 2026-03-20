class Elevator:
	def __init__(self, min_floor, max_floor) -> None:
		self._min_floor = min_floor
		self._max_floor = max_floor
		self._current_floor = self._min_floor

	def move(self, target_floor_number):
		if target_floor_number > self._max_floor or target_floor_number < self._min_floor:
			return
		
		while self._current_floor != target_floor_number:
			if self._current_floor < target_floor_number:
				self._go_up()
			else:
				self._go_down()


	def _go_up(self):
		self._current_floor += 1
		print(self)

	def _go_down(self):
		self._current_floor -= 1
		print(self)
	
	def __str__(self) -> str:
		return f"Current floor: {self._current_floor}"

def main():
	elevator = Elevator(0, 5)
	elevator.move(5)
	elevator.move(0)

main()