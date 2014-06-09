# This class opens a file which records submission data.

import os
import sys

tag = sys.argv[1]
comment = sys.argv[2]
filename = raw_input("Evergreen Login? ")

print("tag= " + tag)
print("comment= " + comment)
print("filename= " + filename)

input_file = open(filename, "r")

names = input_file.readlines()



def subst_repo(target):
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

	tag_found = False

	for line in lines:
		# Do all the replacements
		if (tag in line):
			print("Found! " + tag)
			tag_found = True

	infile = open(infilename, "a")

	for line in lines:
		# Do all the replacements
		if (tag in line):
			tag_header = tag + ":"
			if (tag_header in line):
				print("Skipping because comment already exists for tag " + tag)
				infile.write(line);
				continue
			infile.write(tag_header + comment)
			print("Substituted! " + tag)
			tag_found = True
		else:
			infile.write(line);

	infile.close()

for name in names:
	name = name.strip()
	subst_repo(name);