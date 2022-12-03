elves = []

matches = []

with open("input.txt", "r") as f:
	lines = f.readlines()

mapper = {
	"A": 1,
	"B": 2,
	"C": 3,
	"X": 1,
	"Y": 2,
	"Z": 3
}

for line in lines:
	line = line.strip()
	if line != "":
		matches.append([
			mapper[line[0]],
			mapper[line[-1]]
		])

total_score = 0

counter = 1

for match in matches:
	#print(f"Line {counter:>4}: {match}")
	counter += 1

	total_score += match[1]

	if match[0] == match[1]:
		total_score += 3
	elif (match[1] - match[0]) in [1, -2]:
		total_score += 6


print(total_score)

dec_total_score = 0


counter = 0
# 1 is lose, 2 is draw, 3 is win
for match in matches:
	print(f"Line {counter:>4}: {match}")
	counter += 1

	wanted_value = match[0]

	if match[1] == 1:
		wanted_value -= 1
	elif match[1] == 3:
		wanted_value += 1

	if wanted_value == 0:
		wanted_value = 3
	elif wanted_value == 4:
		wanted_value = 1

	dec_total_score += wanted_value

	if match[0] == wanted_value:
		dec_total_score += 3
	elif (wanted_value - match[0]) in [1, -2]:
		dec_total_score += 6

print(dec_total_score)

# print("Max:", max(counts))

# print(sum(sorted(counts)[-3:]))

#print("Sum of top 3:", sum(sorted(counts)[:-3]))