from subprocess import Popen
import names, sys, os.path

Popen(["mkdir", "grading"])

for student in names.student_info_field("email"):
 Popen(["git", "clone", "git@github.com:evergreen-csf/"+ student +".git", "grading/"+ student])
