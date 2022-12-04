with open("input.txt", "r") as f:
	lines = [line.rstrip() for line in f]

total = 0

total_overlapping = 0

def clamp(low, high, contain_vals, *vals):
	if contain_vals:
		if len(vals) == 2:
			return vals[0] >= low and vals[1] <= high
		else:
			return False
	else:
		for val in vals:
			if low <= val <= high:
				return True
		return False

for line in lines:
	vals = [int(value) for value in line.replace(",", "-").split("-")]
	if clamp(vals[0], vals[1], True, *vals[2:]) or clamp(vals[2], vals[3], True, *vals[:2]):
		total += 1

	if clamp(vals[0], vals[1], False, *vals[2:]) or clamp(vals[2], vals[3], False, *vals[:2]):
		total_overlapping += 1

print(total)
print(total_overlapping)