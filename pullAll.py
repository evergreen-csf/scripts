from subprocess import Popen
import names, sys, os.path

for student in names.student_info_field("email"):
  print("repos/"+student)
  try:
    Popen(["cd","repos/"+student,";","git","pull"])
  except:
    print("Couldn't open grading/"+student)

