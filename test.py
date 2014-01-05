import github, pygithub_scraps

g = github.Github("colinarobinson","July15th")

pygithub_scraps.make_team_for_each_student(g)