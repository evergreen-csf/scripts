from subprocess import Popen
import names, sys, os.path

target = raw_input("Directory to clone repos into? (blank for ./repos/): ")

target = "./repos" if not target else target

for student in names.student_info_field("email"):
 Popen(["git", "clone", "git@github.com:evergreen-csf/"+ student +".git", target +"/"+ student])
 
finished=True
