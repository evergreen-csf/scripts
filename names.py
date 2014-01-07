namedict = {'barrob16': 'Barrob16',
	    'schkyl10': 'schkyl10',
	    'lethi17': 'lethi17',
	    'swecod03': 'swecod03',
	    'kenjos03': 'Jawshouamoua',
	    'gootra28': 'gootra28',
	    'bajdav18': 'BajDav18',
	    'carjus31': 'CarJus31',
	    'jenroy30': 'Ranzear',
	    'aliahm18': 'aliahm',
	    'aarmag22': 'aarmag22',
	    'rawjor18': 'rawjor18',
	    'lauton04': 'lauton04',
	    'gorbra14': 'mmm314159',
	    'ngutro25': 'ngutro25',
	    'kalmar19': 'kalmar19',
	    'barjos05': 'barjos05',
	    'mccale19': 'mccale19',
	    'arnrus09': 'arnrus09',
	    'linzac03': 'linzac03',
            'mennic31': 'Mendelson9',
            'heruli08': 'am0k',
            'saykat03': 'saykat03',
            'edwchr30': 'edwchr30',
            'crohun22': 'crohun22',
            'wagtra12': 'wagtra12',
            'ranste07': 'ranste',
            'clejos10': 'Josephcle7',
            'dohie11': 'dohie11',
            'sanale04': 'sanale04',
            'andbra16': 'andbra16',
            'yunhar04': 'yunhar04',
            'schmat18': 'schmat18',
            'adazac10': 'adazac10',
            'robana07': 'robana07',
            'benbri03': 'BrieannaBenson',
            'spehan01': 'spehan01',
            'cascam07': 'cascam07',
            'stusam07': 'Stubbycat85',
            'bedkev01': 'mechjesus',
            'morjes14': 'jbirdd1',
            'morjac05': 'morjac05',
            'loeand16': 'loeand16',
            'ngungo16': 'ngungo16',
            'ravzac14': 'ravzac14',
            'kimkev08': 'kimkev08',
            'allkei20': 'allkei20',
            'hartra06': 'terns',
            'rancli11': 'rancli11',
            'rozari15': 'rozari15',
            'carros11': 'carros11',
            'farken24': 'farken24',
            'chaale04': 'babywithahat',
            'hefnic26': 'hefnic26',
            'barwhi18': 'barwhi18',
            'hooian24': 'hooian24',
            'golsam27': 'samuel108'}

emails = namedict.keys()

unames = namedict.values()

def email_prediction(lastfirst_name):
  lastname, firstname = tuple(lastfirst_name.split(', '))
  firstname = firstname.split()[0].lower()
  lastname = lastname.lower()
  return lastname[:3] + firstname[:3]

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
	    

studentf_name = 'students_continuing.txt'
outputfile = open('names.txt','w+')

with open(studentf_name) as studentf:
  for student in studentf.readlines():
    print student
    email, name, uname = info_tuple(student)
    outputfile.write(email + " : " + name + " : " + uname + "\n")