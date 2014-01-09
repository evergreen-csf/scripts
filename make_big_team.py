# Apparently the top-level script to call for creating a new GitHub org team

# By import names, apparently some initialization is done to make names.unames
import github, pygithub_scraps, names

# Uncomment and add your own username and password for this to work
# g = github.Github("Username","Password")

csf = g.get_organization("evergreen-csf")

# What does the string "programmers" mean?
big_team = csf.create_team("programmers", permission="push")

# For all the GitHub usernames in names.unames, add them as members to the team
for student in names.unames:
  big_team.add_to_members(g.get_user(student))
