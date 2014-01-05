import github
from github import Github

# to get started:
# http://jacquev6.github.io/PyGithub/introduction.html

# to install:
# pip install pygithub

#add user to all teams
def add_to_all_teams(user, org):
 """
 add_to_all_teams(github.NamedUser.NamedUser, github.Organization.Organization)
 adds user to all teams in the organization
 """

 for team in org.get_teams():
  team.add_to_members(user)
  
def make_team_for_each_student(auth_user):
  from names import namedict
  org = auth_user.get_organization("evergreen-csf")
  faculty = ("colinarobinson","ppham","weissri","numberten")
  faculty = [auth_user.get_user(uname) for uname in faculty]
  for student in namedict:
   try:
    team = org.create_team(student, permission='admin')
    for m in faculty + [auth_user.get_user(namedict[student])]:
      team.add_to_members(m)
    org.create_repo(student, private=True, team_id=team)
    print student
   except github.GithubException as e:
     msg = e
     print msg
   