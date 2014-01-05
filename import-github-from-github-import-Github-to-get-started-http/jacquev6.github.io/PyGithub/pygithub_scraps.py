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
