lines = [line.rstrip() for line in open("input.txt", "r")]

curr_size = 0
total_size = 0

#filepath = dict()

class dir_obj:
	def __init__(self, name, parent = None):
		self.filesizes = []
		self.dirs = dict()

		self.name = name
		self.parent = parent

	def get_filesizes(self):
		return sum(self.filesizes)
	def get_sub(self, wanted_sub):
		return self.dirs[wanted_sub]
	def add_file(self, filesize):
		self.filesizes.append(int(filesize))
	def add_dir(self, dirname):
		self.dirs[dirname] = dir_obj(dirname, parent = self)
	def get_parent(self):
		return self.parent
	def view_tree(self, linestart = ""):
		print(linestart + self.name)
		for filesize in self.filesizes:
			print("  " + linestart + str(filesize))
		for dirname in self.dirs.values():
			dirname.view_tree(linestart + "  ")
	def get_size(self):
		return self.get_filesizes() + sum(self.dirs[subdir_name].get_size() for subdir_name in self.dirs)

def get_sum(this_dir, min_val = 0, max_val = 100000, total = None):
	if total is None:
		total = [0]
	totals = [get_sum(this_dir.dirs[subdir], min_val, max_val, total) for subdir in this_dir.dirs]

	dir_size = sum(totals) + this_dir.get_filesizes()

	if min_val <= dir_size <= max_val:
		total[0] += dir_size

	if this_dir.name == "/":
		return total[0]
	else:
		return dir_size

def make_space(this_dir, capacity, space_wanted):
	space_remaining = capacity - this_dir.get_size()

	space_wanted = space_wanted - space_remaining

	if space_wanted <= 0:
		return 0
	else:
		current_smallest = [-1]
		return make_space_rec(this_dir, space_wanted, current_smallest)

def make_space_rec(this_dir, space_wanted, current_smallest):
	if current_smallest is None:
		current_smallest = [-1]
	
	totals = [make_space_rec(this_dir.dirs[subdir], space_wanted, current_smallest) for subdir in this_dir.dirs]

	dir_size = sum(totals) + this_dir.get_filesizes()

	if space_wanted <= dir_size:
		if current_smallest[0] == -1 or dir_size <= current_smallest[0]:
			current_smallest[0] = dir_size

	if this_dir.name == "/":
		return current_smallest[0]
	else:
		return dir_size

base_dir = dir_obj("/")
current_dir = base_dir

for line in lines:
	if not line or line == "$ cd /":
		continue
	elif line == "$ cd ..":
		current_dir = current_dir.get_parent()
	elif line.startswith("$ cd "):
		current_dir = current_dir.get_sub(line[5:])
	elif line.startswith("dir "):
		current_dir.add_dir(line[4:])
	elif line[:1].isnumeric():
		current_dir.add_file(line.split(" ")[0])

other_sum = 0
for line in lines:
	if any(char.isdigit() for char in line):
		other_sum += int(line.split(" ")[0])
print(other_sum)

print(f"Custom sum: {get_sum(base_dir)}")
print(f"Size of base directory: {base_dir.get_size()}")
print(make_space(base_dir, 70000000, 30000000))

#print(make_space(base_dir, 30000000))
# def get_sum(given_dir):
# 	if curr_size <= 100000:
# 		total_size += curr_size
# 	curr_size = 0
# 	continue