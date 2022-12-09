trees = [list(map(int, list(treeline))) for treeline in [line.rstrip() for line in open("input.txt", "r")]]

def is_visible(trees, row, col):
	if row == 0 or col == 0 or row == len(trees) - 1 or col == len(trees[0]) - 1:
		return True

	given_height = trees[row][col]

	# left/right
	if all([tree < given_height for tree in trees[row][:col]]):
		return True
	if all(tree < given_height for tree in trees[row][col+1:]):
		return True
	
	# up/down
	if all(trees[i][col] < given_height for i in range(row)):
		return True
	if all(trees[i][col] < given_height for i in range(row + 1, len(trees))):
		return True

	# default False
	return False

def get_scenic_score(trees, row, col):
	given_height = trees[row][col]

	# left/right
	left_val = 0
	for i in range(col - 1, 0 - 1,-1):
		left_val += 1 
		if trees[row][i] >= given_height:
			break
		

	right_val = 0
	for i in range(col + 1,len(trees[row])):
		right_val += 1 
		if trees[row][i] >= given_height:
			break
		

	# up/down
	up_val = 0
	for j in range(row - 1, 0 - 1,-1):
		up_val += 1 
		if trees[j][col] >= given_height:
			break
		
	down_val = 0
	for j in range(row + 1,len(trees)):
		down_val += 1 
		if trees[j][col] >= given_height:
			break
		
	return left_val * right_val * down_val * up_val

total_visible = 0
for i in range(len(trees)):
	for j in range(len(trees[0])):
		total_visible += is_visible(trees, i, j)

print(total_visible)

max_score = 0
for i in range(len(trees)):
	for j in range(len(trees[0])):
		score = get_scenic_score(trees, i, j)
		if score > max_score:
			max_score = score
print(max_score)
