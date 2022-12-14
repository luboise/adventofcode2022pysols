class Monkey:
	def __init__(self, items, execstring, modnum, truemonk, falsemonk):
		self.items = items
		self.execstring = execstring
		self.modnum = modnum
		self.truemonk = truemonk
		self.falsemonk = falsemonk

		self.inspectioncount = 0

	def pass_items(self, monkey_list, relief_after_inspection = True, super_mod = None):
		for i in range(len(self.items)):
			self.increment_inspection()
			exec("self.items[0] = " + self.execstring.replace("old", str(self.items[0])))
			
			if relief_after_inspection:
				self.items[0] = self.items[0] // 3

			if super_div is not None:
				self.items[0] %= super_div

			recipient_index = self.get_passing_monkey(self.items[0])
			monkey_list[recipient_index].give_item(self.items.pop(0))

	def get_passing_monkey(self, value):
		if value % self.modnum == 0:
			return self.truemonk
		else:
			return self.falsemonk

	def give_item(self, value):
		self.items.append(value)

	def increment_inspection(self, amount = 1):
		self.inspectioncount += amount

	def get_inspection_count(self):
		return self.inspectioncount

	def get_modnum(self):
		return self.modnum


def get_monkeys_from_file(filename):
	monkeys = []
	
	lines = [line.rstrip() for line in open(filename, "r")]

	i = 0
	while i < len(lines):
		line = lines[i]
		if line.startswith("Monkey"):
			items = [int(worry) for worry in lines[i+1][len("  Starting items: "):].split(", ")]
			execstring = lines[i+2][len("  Operation: new = "):]
			modnum = int(lines[i+3][len("  Test: divisible by "):])
			truemonk = int(lines[i+4][len("    If true: throw to monkey "):])
			falsemonk = int(lines[i+5][len("    If false: throw to monkey "):])

			new_monkey = Monkey(items, execstring, modnum, truemonk, falsemonk)
			monkeys.append(new_monkey)

			i += 7
		else:
			i += 1

	return monkeys

def list_product(in_list):
	total = 1
	for value in in_list:
		total *= value
	return total

monkeys = get_monkeys_from_file("input.txt")

for i in range(20):
	for monkey in monkeys:
		monkey.pass_items(monkeys)
inspection_counts = sorted([monkey.get_inspection_count() for monkey in monkeys])

print(inspection_counts[-2] * inspection_counts[-1])




monkeys = get_monkeys_from_file("input.txt")

super_mod = list_product([monkey.get_modnum() for monkey in monkeys])

for i in range(10000):
	print(f"Round {i+1}")
	for monkey in monkeys:
		monkey.pass_items(monkeys, relief_after_inspection = False, super_mod = super_mod)
inspection_counts = sorted([monkey.get_inspection_count() for monkey in monkeys])
print(inspection_counts[-2] * inspection_counts[-1])

