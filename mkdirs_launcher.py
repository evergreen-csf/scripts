from subprocess import Popen
import names

for student in names.emails:
  Popen(["./mkdirs", student, "../grading/"])
