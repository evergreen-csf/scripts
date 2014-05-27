from subprocess import call
import names, sys, os.path, shlex

for student in names.student_info_field("email"):
  print("repos/"+student)
  try:
    cmd = shlex.split('sh -c "(cd repos/'+student+'; git pull)"')
    call(cmd)
  except (e, msg):
    print("Couldn't open repos/"+student)

