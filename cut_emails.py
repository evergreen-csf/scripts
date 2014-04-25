import sys

# First argument is the file to open / read

filename = raw_input();

file = open (filename, "r");

lines = file.readlines()

# To process a list of email addresses
# and add comma separation

string = ""

for line in lines:
	tokens = line.split() # None separator means any whitespace
	if (len(tokens) > 2):
		string += tokens[2] + ", "

print(string)