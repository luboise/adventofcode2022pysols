def clamp (val, low, high):
	if val > high:
		return high
	elif val < low:
		return low
	else:
		return val

def parse_move_str(move):
	if move.startswith("U"):
		move_x, move_y = 0, 1
	elif move.startswith("D"):
		move_x, move_y = 0, -1
	elif move.startswith("L"):
		move_x, move_y = -1, 0
	elif move.startswith("R"):
		move_x, move_y = 1, 0
	else:
		move_x, move_y = 0, 0

	return move_x, move_y

class ropeNode:
	def __init__(self, startx = 0, starty = 0):
		self.x = 0
		self.y = 0

	def move(self, x, y):
		self.x += x
		self.y += y

	def xy_distance_from(self, other_node):
		return self.x - other_node.x, self.y - other_node.y

	def xy_distance_to(self, other_node):
		return other_node.x - self.x, other_node.y - self.y

	def get_pos(self):
		return self.x, self.y

	def snap_to(self, other_node):
		diff_x, diff_y = self.xy_distance_to(other_node)

		if abs(diff_x) < 2 and abs(diff_y) < 2:
			return self.get_pos()

		move_x = clamp(diff_x, -1, 1)
		move_y = clamp(diff_y, -1, 1)

		self.x += move_x
		self.y += move_y

		return self.get_pos()




moves = [line.rstrip() for line in open("input.txt", "r")]

visited = set()
visited.add((0, 0))

head = ropeNode()
tail = ropeNode()

for move in moves:
	amount = int(move[2:])

	move_x, move_y = parse_move_str(move)
	
	for i in range(abs(amount)):
		head.move(move_x, move_y)
		visited.add(tail.snap_to(head))

print(len(visited))