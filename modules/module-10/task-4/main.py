from car import Car
from competition import Competition

def main():
	cars = create_cars()
	
	competition = Competition("Suuri romuralli", 8000, cars)
	competition.run()

def create_cars() -> list[Car]:
	cars = []

	for i in range(10):
		cars.append(Car(f"ABC-{i + 1}"))
	
	return cars

main()