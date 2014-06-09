# This class searches the given student's eval file
# and appends the given line to the given tag

import os, sys

if (len(sys.argv) < 2):
	
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

tags = set(lines)
tags -= set(['\n'])

text_lines
found_dict = {key: False for key in tags}

for line in lines:
	# Do all the replacements
	for tag in tags:
		if (tag in line):
			print("Found! " + tag)
			found_dict[tag] = True

infile = open(infilename, "a")

infile.write("\n # Tags for automated substitution. Do not edit by hand. \n")
# Go through all tags not found, and add them to end of file
for tag in found_dict.keys():
	if (not found_dict[tag]):
		infile.write(tag + "\n")

infile.close()