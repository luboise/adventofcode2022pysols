with open("input.txt", "r") as f:
	vals_list = [[int(val) for val in line.rstrip().replace(",", "-").split("-")] for line in f.readlines()]

def clamp(low, high, contain_vals, *vals):
	if contain_vals:
		return len(vals) == 2 and low <= vals[0] <= vals[1] <= high
	return any([low <= val <= high for val in vals])

total = len([True for vals in vals_list if clamp(vals[0], vals[1], True, *vals[2:]) or clamp(vals[2], vals[3], True, *vals[:2])])
total_overlapping = len([True for vals in vals_list if clamp(vals[0], vals[1], False, *vals[2:]) or clamp(vals[2], vals[3], False, *vals[:2])])

print(total, total_overlapping, sep = "\n")

# for line in lines:
# 	vals = [int(value) for value in line.replace(",", "-").split("-")]
# 	total += clamp(vals[0], vals[1], True, *vals[2:]) or clamp(vals[2], vals[3], True, *vals[:2])
# 	total_overlapping += clamp(vals[0], vals[1], False, *vals[2:]) or clamp(vals[2], vals[3], False, *vals[:2])

# if clamp(vals[0], vals[1], True, *vals[2:]) or clamp(vals[2], vals[3], True, *vals[:2]):
# 	total += 1

# if clamp(vals[0], vals[1], False, *vals[2:]) or clamp(vals[2], vals[3], False, *vals[:2]):
# 	total_overlapping += 1
