import copy

def parseInput(filename):
	with open(filename, "r") as f:
		stacks = []
		instructions = []

		moving = False

		for line in f:
			# Ensure correct mode for parsing
			line = line.rstrip()
			if not stacks:
				stacks = [list() for i in range((len(line) + 1) // 4)]
			elif line.startswith(" 1") or not line:
				moving = True
				continue

			if moving:
				# Add instruction tuple to stack
				instruction = [int(value) for value in line.split(" ")[1::2]]

				# Fix to/from to be indices
				instruction[1] -= 1
				instruction[2] -= 1

				instructions.append(instruction)
			else:
				# Append current char to appropriate stack
				for i in range(0, (len(line) + 1) // 4):
					char = line[4 * i + 1]
					if char != " ":
						stacks[i] = list(char) + stacks[i]
				

	return stacks, instructions

stacks, instructions = parseInput("input.txt")
stacks2 = copy.deepcopy(stacks)

for instruction in instructions:
	# Adjust stack 1 (problem 1)
	amount, move_from, move_to = tuple(instruction[:3])
	for i in range(amount):
		stacks[move_to].append(stacks[move_from].pop())

	# Adjust stack 2 (problem 2)
	start_index = len(stacks2[move_from]) - amount
	stacks2[move_to] = stacks2[move_to] + stacks2[move_from][start_index:]
	stacks2[move_from] = stacks2[move_from][:start_index]

print(*[stack[-1] for stack in stacks if len(stack)], sep = "")
print(*[stack[-1] for stack in stacks2 if len(stack)], sep = "")
