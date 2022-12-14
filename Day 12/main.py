import numpy as np

start = None
end = None

lines = [line.rstrip() for line in open("input.txt", "r")]
for row_i in range(len(lines)):
	row = lines[row_i]

	new_row = []
	for column_j in range(len(row)):
		char = row[column_j]

		if start is None and char == "S":
			start = (row_i, column_j)
			new_row.append(1)
		elif end is None and char == "E":
			end = (row_i, column_j)
			new_row.append(26)
		else:
			new_row.append(ord(char) - 96)

	lines[row_i] = new_row



array = np.array(lines)
connecting_matrix = np.zeros((array.size, array.size), dtype = np.bool_)

row_count = array.shape[0]
col_count = array.shape[1]

def get_array_pos(i, j, col_count):
	return i * col_count + j

for i in range(row_count):
	for j in range(col_count):	
		# Left
		if 0 <= j-1 < col_count:
			if -1 <= array[i][j] - array[i][j-1] <= 1:
				connecting_matrix[get_array_pos(i, j, col_count)][get_array_pos(i, j-1, col_count)] = True
				
		
		# Right
		if 0 <= j+1 < col_count:
			if -1 <= array[i][j] - array[i][j+1] <= 1:
				connecting_matrix[get_array_pos(i, j, col_count)][get_array_pos(i, j+1, col_count)] = True

		# Down
		if 0 <= i+1 < row_count:
			if -1 <= array[i][j] - array[i+1][j] <= 1:
				connecting_matrix[get_array_pos(i, j, col_count)][get_array_pos(i+1, j, col_count)] = True
		
		# Up
		if 0 <= i-1 < row_count:
			if -1 <= array[i][j] - array[i-1][j] <= 1:
				connecting_matrix[get_array_pos(i, j, col_count)][get_array_pos(i-1, j, col_count)] = True


count = 1

matrix_copy = connecting_matrix.copy()
while not matrix_copy[get_array_pos(start[0], start[1], col_count)][get_array_pos(end[0], end[1], col_count)]:
	print(f"Step length {count} failed")
	count += 1
	matrix_copy = np.dot(matrix_copy, connecting_matrix)

print(f"Smallest amount of steps needed: {count}")

# nplines = np.fromfile("input.txt", dtype = np.string_)
# print(char_count)