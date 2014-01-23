with open('names.txt') as nfile:
 student_info_tuples = [tuple(line.split(' : ')) for line in nfile.readlines()]

def student_info_dict(key, value):
  """
  student_info_dict(key, value) -> {key : value} for each student
  possible values for key and value are 'email', 'name', and 'github'
  """
  fieldmap = {"email" : 0, "name" : 1, "github" : 2}
  key = fieldmap[key]
  value = fieldmap[value]
  
  return {student[key] : student[value] for student in student_info_tuples}

# Where does the dictionary 'student' come from?
def student_info_field(field)
  fieldmap = {"email" : 0, "name" : 1, "github" : 2}
  field = fieldmap[field]
  return (student[field] for student in student_info_tuples)

# Predicts the e-mail by using Evergreen formula of:
# First three letters of last name,
# first three letters of first name,
# arbitrary two-digit number
# This must somehow be used with e-mails.txt later to come up with
# two digit number.
def email_prediction(lastfirst_name):
  lastname, firstname = tuple(lastfirst_name.split(', '))
  firstname = firstname.split()[0].lower()
  lastname = lastname.lower()
  return lastname[:3] + firstname[:3]

# Where does namedict come from?
def info_tuple(student_name):
  potential_emails = [email for email in emails if email.startswith(email_prediction(student))]
  
  if len(potential_emails) is 1:
    return (potential_emails[0], student_name, namedict[potential_emails[0]])
  elif len(potential_emails) is 0:
    print "No email/uname pair found for student:", student_name
    return (raw_input("Enter email to use, or NONE if not known: "),
	    student_name,
	    raw_input("Enter github username, or NONE if not known: "))
  else:
    print "Potential emails found for", student_name + ":", [(email, namedict(email)) for email in potential_emails]
    return (raw_input("Enter email to use: "),
	    student_name,
	    raw_input("Enter github username: "))

# Creates the file students_continuing.txt as a list of colon-delimeted
# tuples of e-mail address, full name, and Github username	    
def gen_namefile()
 studentf_name = 'students_continuing.txt'
 outputfile = open('names.txt','w+')

 with open(studentf_name) as studentf:
  for student in studentf.readlines():
    print student
    email, name, uname = info_tuple(student)
    outputfile.write(email + " : " + name + " : " + uname + "\n")
 outputfile.close()
