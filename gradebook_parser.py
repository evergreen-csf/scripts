'''
okay
I have a csv with rows for each student and columns for id, name, and various homework assignments
the hw assignment rows contain a value corresponding to a 'grade' for that assignment, 
or yes/no for attendence.

I want to read this file to extract some particular things from it:
 - each student's id, which is also their github repo
 - the corresponding attendance statistics
 - the names of each of the assignments
 
I will take this information and insert it into each student's eval.txt
 - turn the assignment/session name into a tag ({W1} : week one goals compelete, self-eval done)
 - put in a tag for each non-null assignment in the spreadsheet
'''
from __future__ import print_function
from csv import DictReader
from sys import argv
from subprocess import Popen
from glob import glob

usage = "usage: %s <gradebook csv file>" % argv[0]
if __name__ is not "__main__":
  argv = argv[-2:]

if len(argv) is not 2:
  print(usage)
  quit()

header_tag_dict = {"Sem" : "S",
                   "Talk" : "SS"}
  
try:
  gradebookfile = open(argv[1])
except IOError, (ErrorNumber, ErrorMessage):
  if ErrorNumber == 2: #File not found
    print("File %s not found." % argv[1])
    quit()
  else:
    print(ErrorMessage)
    quit()

gradebook = DictReader(gradebookfile)
assignments_with_tags = set()
for field in gradebook.fieldnames:
  for assignment in header_tag_dict:
    if assignment in field:
      assignments_with_tags.add((field,
				 header_tag_dict[assignment],
				 ''.join(filter(lambda x: x.isdigit(), field))) #the first digit to appear in the field title is assumed to be the serial number
				)
#eval(input(str(assignments_with_tags)+"\nDoes this look correct? quit() if not. "))
gradebook = {student["Evergreen Login"].strip(): student for student in gradebook}
gradebookfile.close()

'''
for student in gradebook, open that student's eval.txt and put in a tag
 for all assignments that have tags
 
for each assignment in gradebook, check if its prefix is in header_tag_dict
 if it is, 
'''

import cloneAll, names

for student in gradebook:
  try:
    target = glob(cloneAll.target+"/"+student+"/prog/*eval.txt")[0]
    evalfile = open(target, "r")
  except IOError, (ErrorNumber, ErrorMessage):
    if ErrorNumber == 2: #File not found
      print("File %s not found." % argv[1])
      quit()
    else:
      print(ErrorMessage)
      quit()
  except IndexError, ErrorMessage:
    print("%s: Eval file at %s not found." % (ErrorMessage, cloneAll.target+"/"+student+"/prog/*eval.txt"))
    continue
  
  tags = set(evalfile.read().splitlines())
  tags -= set(['\n'])
  evalfile.close()
  for assignment in assignments_with_tags:
    if gradebook[student][assignment[0]].strip() is not '':
      tags.add('{'+assignment[1]+assignment[2]+'} : '+assignment[0])
  evalfile = open(target, 'w')
  evalfile.write('\n'.join(sorted(tags)))
  evalfile.close()
