# This class searches the given student's eval file
# and populates it with tags if they are not already found.

import os

target = raw_input("Evergreen Login? ")

target = "." if not target else target

repos_dir = "repos"

infilename = repos_dir + "/" + target + "/prog/"+target+"-eval.txt"

try:
	infile = open(infilename, "r")
except IOError, (ErrorNumber, ErrorMessage):
	if ErrorNumber == 2: # file not found
		print("Creating " + infilename + " because it does not exist")
		infile = open(infilename, "w")
		infile.writelines([])
		infile.close()
		infile = open(infilename, "r")

lines = infile.readlines()
infile.close()

tags = ["{W"+str(i)+"}" for i in range(1,11)]
print(tags)

found_dict = {key: False for key in tags}

for line in lines:
	# Do all the replacements
	for tag in tags:
		if (tag in line):
			print("Found! " + tag)
			found_dict[tag] = True

infile = open(infilename, "a")
# Go through all tags not found, and add them to end of file
for tag in found_dict.keys():
	if (not found_dict[tag]):
		infile.write(tag + "\n")

infile.close()