import sys

# First argument is the file to open / read

filename = raw_input();

file = open (filename, "r");

lines = file.readlines()

for line in lines:
	tokens = line.split(":")
	print(tokens[0])
