def get_sum(numbers) -> int:
	sum = 0

	for i in numbers:
		sum += i
	
	return sum

def main():
	numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

	print(f"List: {numbers}")
	print(f"Sum: {get_sum(numbers)}")

main()