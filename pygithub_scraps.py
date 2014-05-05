from __future__ import print_function
import github, getpass, names
from github import Github

# to get started:
# http://jacquev6.github.io/PyGithub/introduction.html

# to install:
# pip install pygithub

####
# Stuff from names.py
name_login_dict = names.student_info_dict("email", "github") # returns dict mapping emails to github unames
login_name_dict = names.student_info_dict("github", "email")

print("pygithub needs github login info to work")
g = github.Github(raw_input("Username: "), getpass.getpass("Password: "))
print("This is going to take a second to load; we're doing a bunch of api calls.")

print("getting organization 'evergreen-csf'")
csf = g.get_organization("evergreen-csf")

print("getting teams")
teams = csf.get_teams()
team_id_dict = {team.name : team for team in teams}

print("getting member list")
members = set(csf.get_members())
m_names = set([m.login for m in members])

print("finding faculty and TAs")
faculty = set()
fac_objs = team_id_dict["Owners"].get_members()
for m in members:
  if m.login in [f.login for f in fac_objs]:
    faculty.add(m)

f_names = set([f.login for f in faculty])

print("finding students")
students = members - faculty
s_names = set([s.login for s in students])
students_by_name = {name : obj for name in s_names for obj in students if name == obj.login}

def all_students_have_teams():
 print("checking if all students are assigned teams...")
 students_without_teams = students.copy()
 for team in teams:
  if team.name != 'programmers':
   try:
     for s in team.get_members():
       if s.login not in f_names:
         students_without_teams.remove(students_by_name[s.login])
   except KeyError as err:
     print(s.login)
    
 students_with_teams = students - students_without_teams
 return students_with_teams, students_without_teams

if (raw_input('any character to check that all students have teams, enter to skip') != ''):
 students_with_teams, students_without_teams = all_students_have_teams()
 if len(students_without_teams):
   print("the following students are not in any teams:")
   print([s.login for s in students_without_teams])

def make_team_for_student(student):
 try:
  t = csf.create_team(login_name_dict[student.login], permission='admin')
  t.add_to_members(student)
  for f in faculty:
    t.add_to_members(f)
  t.add_to_repos(csf.get_repo(t.name))
 except github.GithubException as e:
   msg = e
   print(student.login, t.name, msg)
 except KeyError:
   print(student.login, t.name)
  
def make_team_for_students_without_teams():
  for student in students_without_teams:
    make_team_for_student(student)
    students_without_teams.remove(student)
    students_with_teams.add(student)

## This code was desinged to be fairly general, where the above is specifically for evergreen-csf
## That makes it easier to see, I think, the principles of what's going on
## It also makes the code pretty slow, and means we can't take advantage of the caching
##  on load from earlier.


#add user to all teams
def add_to_all_teams(user, org):
 """
 add_to_all_teams(github.NamedUser.NamedUser, github.Organization.Organization)
 adds user to all teams in the organization
 """

 for team in org.get_teams():
  team.add_to_members(user)


def make_team_for_each_student(auth_user):
  for student in name_login_dict:
   try:
    team = csf.create_team(student, permission='admin')
    for m in faculty + [auth_user.get_user(namedict[student])]:
      team.add_to_members(m)
    csf.create_repo(student, private=True, team_id=team)
    print(student)
   except github.GithubException as e:
     msg = e
     print(msg)

def make_big_team(auth_user):
  """
  probably single-use function to make a single big team for all of csf
  """
  big_team = csf.create_team("programmers", permission="push")

  for student in names.unames:
    big_team.add_to_members(g.get_user(student))
