def convert_to_litres(galloons) -> float:
	liter_multiplier = 3.78541

	return float(galloons) * (liter_multiplier)

def main():
	litres = 0

	while litres >= 0:
		litres = convert_to_litres(input("Enter galloons: "))
		print(f"Litres: {litres}")

main()