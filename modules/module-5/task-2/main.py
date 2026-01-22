end_command = ""
user_input = None

numbers = []
biggest_numbers = []

while (user_input != end_command):
	user_input = input("Enter number: ")
	numbers.append(user_input)

numbersCount = 5

numbers.sort(reverse=True)

for i in range(numbersCount):
	print(numbers[i])