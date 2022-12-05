with open("input.txt", "r") as f:
	lines = [line.rstrip() for line in f]

stacks = []
moving = False

for line in lines:
	if not line:
		continue
	elif not stacks:
		stacks = [list() for i in range((len(line) + 1) // 4)]
	elif line.startswith(" 1"):
		moving = True
		continue


	if moving:
		amount, move_from, move_to = tuple([int(value) for value in line[5:].replace("from ", "").replace("to ", "").split(" ")])

		for i in range(amount):
			stacks[move_to - 1].append(stacks[move_from - 1].pop())
	else:
		for i in range(0, (len(line) + 1) // 4):
			char = line[4 * i + 1]
			if char != " ":
				stacks[i] = list(char) + stacks[i]
	
stacks2 = []
moving = False

for line in lines:
	if not line:
		continue
	elif not stacks2:
		stacks2 = [list() for i in range((len(line) + 1) // 4)]
	elif line.startswith(" 1"):
		moving = True
		continue


	if moving:
		amount, move_from, move_to = tuple([int(value) for value in line[5:].replace("from ", "").replace("to ", "").split(" ")])

		move_from -= 1
		move_to -= 1

		start_index = len(stacks2[move_from]) - amount

		stacks2[move_to] = stacks2[move_to] + stacks2[move_from][start_index:]
		stacks2[move_from] = stacks2[move_from][:start_index]
	else:
		for i in range(0, (len(line) + 1) // 4):
			char = line[4 * i + 1]
			if char != " ":
				stacks2[i] = list(char) + stacks2[i]

to_print = [stack[-1] for stack in stacks if len(stack)]
print(*to_print, sep = "")

to_print2 = [stack[-1] if len(stack) else " " for stack in stacks2]
print(*to_print2, sep = "")
