class Elevator:
	def __init__(self, min_floor, max_floor) -> None:
		self._min_floor = min_floor
		self._max_floor = max_floor
		self._current_floor = self._min_floor

	def move(self, target_floor):
		if target_floor > self._max_floor or target_floor < self._min_floor:
			return
		
		while self._current_floor != target_floor:
			if self._current_floor < target_floor:
				self._go_up()
			else:
				self._go_down()
				
	def reset(self):
		self.move(self._min_floor)

	def _go_up(self):
		self._current_floor += 1
		print(self)

	def _go_down(self):
		self._current_floor -= 1
		print(self)
	
	def __str__(self) -> str:
		return f"Elevator: {id(self)} | Current floor: {self._current_floor}"

class Building:
	def __init__(self, elevator_count: int, min_floor: int, max_floor: int) -> None:
		self._elevator_count = elevator_count
		self._min_floor = min_floor
		self._max_floor = max_floor
		self._elevators = self._create_elevators()
	
	def move_elevator(self, elevator_id: int, target_floor: int):
		if elevator_id >= len(self._elevators) or elevator_id < 0:
			return

		self._elevators[elevator_id].move(target_floor)
	
	def alarm(self):
		print("FIREEE!!!")

		for elevator in self._elevators:
			elevator.reset()

	def _create_elevators(self) -> list[Elevator]:
		elevators = []

		for i in range(self._elevator_count):
			elevators.append(Elevator(self._min_floor, self._max_floor))
		
		return elevators

def main():
	building = Building(3, 0, 6)

	building.move_elevator(0, 2)
	building.move_elevator(1, 5)
	building.move_elevator(2, 4)

	building.alarm()

main()