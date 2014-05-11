# subprocess is the built-in python library for spawning processes
from subprocess import Popen
import names

# http://docs.python.org/2/library/subprocess.html#popen-constructor

# I guess this calls the scrap mkdir on each student e-mail / Evergreen ID,
# since we have chosen to name repos after the IDs.
# But what is "../grading/"? An output directory one directory level up?
# Oh, these are the arguments to call to the script,
# and it's in spawned processes because the scraps must take a long time to
# complete, and you don't want to block on them.
#for student in names.emails:
#  Popen(["./mkdirs", student, "../grading/"])
for student in ("model"): # names.student_info_field("email"):
  #altered for Spring quarter
  Popen(["./spring_mkdirs", student, "../grading/"])
