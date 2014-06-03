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
                   "Talk" : "SS",
		   "A Workshop" : "AWK",
		   "A hw" : "AHW",
		   "A lab" : "ALAB",
		   "Arch Midterm" : "AMID",
		   "Soft" : "ANTH",
		   "Group" : "MTG",
		   "Worksheet" : "PWK"}

arch_tags = ("AWK", "ALAB", "AHW", "AMID")
sem_tags = ("S", "SS")
prog_tags = ("PWK", "L", "C", "W")
anthro_tags = ("ANTH")
secnames = ["sem", "prog", "arch"] #### This is an important line. only sections listed here will be graded
				   ####
secnames_to_tags = {"sem" : sem_tags,
		    "arch" : arch_tags,
		    "prog" : prog_tags,
		    "anth" : anthro_tags}
  
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
in_sec = (lambda tag, sec : True in map(lambda s : tag.startswith('{'+s), sec))
def ones_in_sec(tags, secname):
  return filter(lambda t: in_sec(t, secnames_to_tags[secname]), tags)

import cloneAll, names

for student in gradebook:
  evalfiles = []
  notfound = []
  for sec in secnames:
    try: 
      target = cloneAll.target+"/"+student+"/"+sec+"/"+student+"-eval.txt"
      evalfiles.append(open(target, 'r'))
    
    except IOError, (ErrorNumber, ErrorMessage):
      if ErrorNumber == 2: #File not found
        print("File %s not found." % target)
        notfound.append(sec)
      else:
        print(ErrorMessage)
        quit()
  

  tags = set()
  for evalfile in evalfiles:
    tags |= set(evalfile.read().splitlines())
    tags -= set(['\n'])
    evalfile.close()
    
  for assignment in assignments_with_tags:
    if gradebook[student][assignment[0]].strip() is not '':
      tags.add('{'+assignment[1]+assignment[2]+'} : '+assignment[0])
      
  for sec in secnames:
    if sec in notfound:
      continue
    evalfile = open(cloneAll.target+"/"+student+"/"+sec+"/"+student+"-eval.txt", 'w')
    evalfile.write('\n'.join(sorted(ones_in_sec(tags, sec))))
    evalfile.close()