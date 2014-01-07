import github, pygithub_scraps, names

# g = github.Github("Username","Password")

csf = g.get_organization("evergreen-csf")

big_team = csf.create_team("programmers", permission="push")

for student in names.unames:
  big_team.add_to_members(g.get_user(student))
