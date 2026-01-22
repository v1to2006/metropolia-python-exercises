import random

throw_count = int(input("Enter dice throw amount: "))

sum = 0

for i in range(throw_count):
	sum += random.randint(1, 6)

print(f"Average: {sum / throw_count}")