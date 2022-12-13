lines = [line.rstrip() for line in open("input.txt", "r")]

class Monkey:
	def __init__(self, items, execstring, divnum, truemonk, falsemonk):
		self.items = items
		self.execstring = execstring
		self.divnum = divnum
		self.truemonk = truemonk
		self.falsemonk = falsemonk

monkeys = []

i = 0
while i < len(lines):
	line = lines[i]
	if line.startswith("Monkey"):
		items = [int(worry) for worry in lines[i+1][len("  Starting items: "):].split(", ")]
		execstring = lines[i+2][len("  Operation: new = "):]
		divnum = int(lines[i+3][len("  Test: divisible by "):])
		truemonk = int(lines[i+4][len("    If true: throw to monkey "):])
		falsemonk = int(lines[i+5][len("    If false: throw to monkey "):])

		new_monkey = Monkey(items, execstring, divnum, truemonk, falsemonk)
		monkeys.append(new_monkey)

		i += 7
	else:
		i += 1

print(monkeys)
