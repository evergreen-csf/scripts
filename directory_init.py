import names
from subprocess import Popen

"""
Python launcher for make-empty-repo, a shell script which, as you might guess, creates an empty repo
This file exists for simple access to names.py, and to factor out the process of selecting students to make repos for
  from the process of making the repos themselves.
"""

for student in names.emails:
 Popen(["./make-empty-repo", student, "../grading"])
