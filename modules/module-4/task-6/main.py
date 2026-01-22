import random

random_points_count = int(input("Enter random points count: "))
hit_circle_counter = 0

currentIndex = random_points_count

while currentIndex != 0:
	random_point = [float(random.randint(-100, 100)) / 100, float(random.randint(-100, 100)) / 100]

	print(random_point)

	if random_point[0] ** 2 + random_point[1] ** 2 < 1:
		hit_circle_counter += 1
	
	currentIndex -= 1

pi_ratio = 4 * hit_circle_counter / random_points_count

print(f"PI Ratio: {pi_ratio}")