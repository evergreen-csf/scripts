import sys

# First argument is the file to open / read

filename = raw_input();

file = open (filename, "r");

lines = file.readlines()

# To process a list of email addresses
# and add comma separation

string = ""

for line in lines:
	line = line.strip() + "@evergreen.edu;"
	string += line

print(string)