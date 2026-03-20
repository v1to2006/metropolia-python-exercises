from car import Car
from competition import Competition

players = [
			Car("ABC-0"),
			Car("ABC-1"),
			Car("ABC-2"),
			Car("ABC-3"),
			Car("ABC-4"),
			Car("ABC-5"),
			Car("ABC-6"),
			Car("ABC-7"),
			Car("ABC-8"),
			Car("ABC-9"),
			]

def main():
	competition = Competition(players)
	competition.run()

main()