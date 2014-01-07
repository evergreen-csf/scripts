import names
from subprocess import Popen

for student in names.emails:
 Popen(["./make-empty-repo", student, "../grading"])
