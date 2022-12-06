datastream = open("input.txt", "r").read().rstrip()

marker_len = 4

for i in range(len(datastream) - marker_len):
	chunk = datastream[i:i+marker_len]
	if len(set(chunk)) == marker_len:
		print(f"Marker from char {i+1} to char {i + marker_len}")
		break
else:
	print("Marker not found.")