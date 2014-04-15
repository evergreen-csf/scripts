file = open ("dct-class-list.txt", "r");

lines = file.readlines()

for line in lines:
	tokens = line.split(" ")
	print(tokens[0] + " " + tokens[1])
