from subprocess import Popen
import names

for student in ("model"): # names.student_info_field("email"):
  #altered for Spring quarter
  Popen(["./spring_mkdirs", student, "../grading/"])
