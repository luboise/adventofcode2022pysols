with open("input.txt", "r") as f:
	lines = [line.rstrip() for line in f]

def getPrio(inchar):
	thisord = ord(inchar)

	if 65 <= thisord <= 90:
		return thisord - 64 + 26
	elif 97 <= thisord <= 122:
		return thisord - 96
	else:
		print(f"Invalid char given: {inchar}")

total_prio = 0

for line in lines:
	half = int((len(line) + 0.5) // 2)
	set1 = set(line[:half])
	set2 = set(line[half:])

	common_char = set1.intersection(set2).pop()
	total_prio += getPrio(common_char)

print(total_prio)

group_prio = 0

for i in range(0, len(lines), 3):
	badge_char = set(lines[i]).intersection(set(lines[i+1]).intersection(set(lines[i+2]))).pop()
	print(badge_char)
	group_prio += getPrio(badge_char)

print(group_prio)