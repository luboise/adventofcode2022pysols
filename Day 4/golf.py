vals_list = [[int(val) for val in line.rstrip().replace(",", "-").split("-")] for line in open("input.txt", "r")]

def clamp(low, high, contain_vals, *vals):
	return contain_vals and (len(vals) == 2 and low <= vals[0] <= vals[1] <= high) or (not contain_vals) and any([low <= val <= high for val in vals])

print(sum([clamp(vals[0], vals[1], True, *vals[2:]) or clamp(vals[2], vals[3], True, *vals[:2]) for vals in vals_list]), sum([clamp(vals[0], vals[1], False, *vals[2:]) or clamp(vals[2], vals[3], False, *vals[:2]) for vals in vals_list]), sep = "\n")

# for line in lines:
# 	vals = [int(value) for value in line.replace(",", "-").split("-")]
# 	total += clamp(vals[0], vals[1], True, *vals[2:]) or clamp(vals[2], vals[3], True, *vals[:2])
# 	total_overlapping += clamp(vals[0], vals[1], False, *vals[2:]) or clamp(vals[2], vals[3], False, *vals[:2])

# if clamp(vals[0], vals[1], True, *vals[2:]) or clamp(vals[2], vals[3], True, *vals[:2]):
# 	total += 1

# if clamp(vals[0], vals[1], False, *vals[2:]) or clamp(vals[2], vals[3], False, *vals[:2]):
# 	total_overlapping += 1
