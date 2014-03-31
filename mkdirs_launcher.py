from subprocess import Popen
import names

for student in names.emails:
  #altered for Spring quarter
  Popen(["./spring_mkdirs", student, "../grading/"])
