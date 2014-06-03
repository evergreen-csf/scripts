from subprocess import call
import names

for student in ["model"]: # names.student_info_field("email"):
  #altered for Spring quarter
  call(["./mkdirs", student, "../repos/"])
