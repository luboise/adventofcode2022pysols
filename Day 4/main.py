with open("input.txt", "r") as f:
	lines = [line.rstrip() for line in f]

total = 0

total_overlapping = 0

for line in lines:
	vals = [int(value) for value in line.replace(",", "-").split("-")]
	if vals[0] <= vals[2] <= vals[1] and vals[0] <= vals[3] <= vals[1] or vals[2] <= vals[0] <= vals[3] and vals[2] <= vals[1] <= vals[3]:
		total += 1

	if vals[0] <= vals[2] <= vals[1] or vals[0] <= vals[3] <= vals[1] or vals[2] <= vals[0] <= vals[3] or vals[2] <= vals[1] <= vals[3]:
		total_overlapping += 1

print(total)
print(total_overlapping)