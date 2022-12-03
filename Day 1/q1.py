elves = []

elf = []

with open("input.txt", "r") as f:
	lines = f.readlines()

for line in lines:
	line = line.strip()
	if line != "":
		elf.append(int(line))
	else:
		elves.append(elf)
		elf = []

if elf:
	elves.append(elf)
	elf = []

counts = [sum(elf) for elf in elves]

print("Max:", max(counts))

print(sum(sorted(counts)[-3:]))

#print("Sum of top 3:", sum(sorted(counts)[:-3]))