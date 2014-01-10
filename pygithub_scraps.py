import github, getpass, names
from github import Github

# to get started:
# http://jacquev6.github.io/PyGithub/introduction.html

# to install:
# pip install pygithub

print "pygithub needs github login info to work"
g = github.Github(raw_input("Username :"), getpass.getpass("Password: "))

csf = g.get_organization("evergreen-csf")

#add user to all teams
def add_to_all_teams(user, org):
 """
 add_to_all_teams(github.NamedUser.NamedUser, github.Organization.Organization)
 adds user to all teams in the organization
 """

 for team in org.get_teams():
  team.add_to_members(user)


def make_team_for_each_student(auth_user):
  namedict = names.student_info_dict("email", "github") # returns dict mapping emails to github unames
  for student in namedict:
   try:
    team = csf.create_team(student, permission='admin')
    for m in faculty + [auth_user.get_user(namedict[student])]:
      team.add_to_members(m)
    csf.create_repo(student, private=True, team_id=team)
    print student
   except github.GithubException as e:
     msg = e
     print msg


def make_big_team(auth_user):
  """
  probably single-use function to make a single big team for all of csf
  """
  big_team = csf.create_team("programmers", permission="push")

  for student in names.unames:
    big_team.add_to_members(g.get_user(student))
