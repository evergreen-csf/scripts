from subprocess import Popen
import names, sys, os.path


for student in names.student_info_field("email"):
    Popen(["echo ", "grading/"+student, ";", "cd","grading/"+student,";","git","pull"])

