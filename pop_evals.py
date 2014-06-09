# This class applies a line to the given student's eval file
# if it doesn't already exist.
# It is meant to be idempotent.
# Currently the line to add is hardcoded, but this could change
# in the future.
# This still requires a separate script to populate eval files with tags
# of the form {HW1}.

import os

target = raw_input("Evergreen Login? ")

target = "." if not target else target

repos_dir = "repos"

infilename = repos_dir + "/" + target + "/prog/"+target+"-eval.txt"
outfilename = infilename+".out"

try:
	infile = open(infilename, "r")
except IOError, (ErrorNumber, ErrorMessage):
	if ErrorNumber == 2: # file not found
		print("Creating " + infilename + " because it does not exist")
		infile = open(infilename, "w")
		infile.writelines([])
		infile.close()
		infile = open(infilename, "r")

outfile = open(outfilename, "w")
lines = infile.readlines()

replacements = [("{HW1}", "has completed Homework 1.")]

for line in lines:
	# Do all the replacements
	for (key, sentence) in replacements:
		if (key in line):
			print("Found! " + key)
			line = sentence
	outfile.write(line)

infile.close()
outfile.close()

os.rename(outfilename, infilename)
