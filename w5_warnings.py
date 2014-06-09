from __future__ import print_function
import cloneAll, names, glob

warnings = []
safe = []

for student in names.student_info_field('email'):
  try:
    target = glob.glob(cloneAll.target+"/"+student+"/prog/*eval.txt")[0]
    evalfile = open(target, "r")
  except IOError, (ErrorNumber, ErrorMessage):
    if ErrorNumber == 2: #File not found
      print("File %s not found." % argv[1])
      quit()
    else:
      print(ErrorMessage)
      quit()
  except IndexError, ErrorMessage:
    print("%s: Eval file at %s not found." % (ErrorMessage, cloneAll.target+"/"+student+"/prog/*eval.txt"))
    continue

  def goals_pred(t):
    return t.startswith('{L') 
  
  def ijava_pred(t):
    return t.startswith('{C')
  
  tags = set(evalfile.read().splitlines())
  evalfile.close()
  tags -= set(['\n'])
  goals = filter(goals_pred, tags)
  ijava = filter(ijava_pred, tags)
  
  if len(goals) < 4 > len(ijava):
    warnings.append((student, max((len(goals), len(ijava)))))
  else:
    safe.append(student)
    
print ("Warning", warnings, "Safe", safe)
    