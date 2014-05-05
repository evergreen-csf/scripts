from subprocess import Popen

nfile = open("staff/data/14s/DCT-names.txt",'r')
student_info_tuples = [tuple(line.split(' : ')) for line in nfile.readlines()]
nfile.close()

def student_info_dict(key, value):
  """
  student_info_dict(key, value) -> {key : value} for each student
  possible values for key and value are 'email', 'name', and 'github'
  """
  fieldmap = {"email" : 0, "name" : 1, "github" : 2}
  key = fieldmap[key]
  value = fieldmap[value]
  
  return {student[key] : student[value] for student in student_info_tuples}
  

def student_info_field(field):
  fieldmap = {"email" : 0, "name" : 1, "github" : 2}
  field = fieldmap[field]
  return (student[field] for student in student_info_tuples)

for student in student_info_tuples:
 Popen(["cp","../DCT/c"+student[0]+"/*","../DCT/"+student[0]+"/prog/"])