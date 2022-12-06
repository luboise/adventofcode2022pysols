def marker_finder(marker_len, filename):
	datastream = open(filename, "r").read().rstrip()
	for i in range(len(datastream) - marker_len):
		chunk = datastream[i:i+marker_len]
		if len(set(chunk)) == marker_len:
			print(f"Marker from char {i+1} to char {i + marker_len}")
			break
	else:
		print("Marker not found.")

marker_finder(4, "input.txt")
marker_finder(14, "input.txt")
