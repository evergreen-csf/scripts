from subprocess import Popen, STDOUT, STDERR
import names, sys, os.path, shlex

for student in names.student_info_field("email"):
  print("repos/"+student)
  try:
    cmd = shlex.split('sh -c "(cd repos/'+student+'; git pull)"')
    Popen(cmd)
  except (e, msg):
    print("Couldn't open repos/"+student)

