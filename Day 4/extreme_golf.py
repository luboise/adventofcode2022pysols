print(sum([(vals[2] <= vals[0] <= vals[1] <= vals[3] or vals[0] <= vals[2] <= vals[3] <= vals[1]) for vals in [[int(val) for val in line.rstrip().replace(",", "-").split("-")] for line in open("input.txt", "r")]]), sum([any([vals[0] <= val <= vals[1] for val in vals[2:]]) or any([vals[2] <= val <= vals[3] for val in vals[:2]]) for vals in [[int(val) for val in line.rstrip().replace(",", "-").split("-")] for line in open("input.txt", "r")]]), sep = "\n")