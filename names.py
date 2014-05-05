__p = raw_input("Path to name file (./staff/data/14s/names.txt'): ")
with open(__p if __p != '' else 'staff/data/14s/names.txt') as nfile:
 student_info_tuples = [tuple(line.strip('\n').split(' : ')) for line in nfile.readlines()]
 

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
  

def email_prediction(lastfirst_name):
  lastname, firstname = tuple(lastfirst_name.split(', '))
  firstname = firstname.split()[0].lower()
  lastname = lastname.lower()
  return lastname[:3] + firstname[:3]
  

def info_tuple(student_name):
  """
  takes a student's name (as it appears in the middle column of names.txt: Last, First [M])
    and produces (email, name, uname), with some input if it gets stuck
  """
  potential_emails = [email for email in student_info_field("email") if email.startswith(email_prediction(student_name))]
  namedict = student_info_dict("email", "github")
  
  if len(potential_emails) is 1:
    return (potential_emails[0], student_name, namedict[potential_emails[0]])
    
  elif len(potential_emails) is 0:
    print( "No email/uname pair found for student:", student_name )
    return (raw_input("Enter email to use, or NONE if not known: "),
	    student_name,
	    raw_input("Enter github username, or NONE if not known: "))
	    
  else:
    print ("Potential emails found for", student_name + ":", [(email, namedict[email]) for email in potential_emails])
    return (raw_input("Enter email to use: "),
	    student_name,
	    raw_input("Enter github username: "))
