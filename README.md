scripts
=======

Scripts for managing Computer Science Foundations stuff.

notes:
---

names.txt
 - source for access to student email/ID, name, and github username; useful for writing scripts of various sorts
 - I'll try to keep this up-to-date as the class continues

pygithub
 - this is the package I'm using for access to the github api through python. docs at http://jacquev6.github.io/PyGithub/
 - install with

    pip install pygithub
    
 - import with 

    import github
    
pygithub_scraps.py
 - the file containing all my work to automate github administration using pygithub.
 - WIP, so bear with me. If you think something should be in there that isn't, feel free to add it
 - if you feel something should be changed or removed, ask me about it first--in case I've written something somewhere that depends on it.
 - upon importing, will ask for your github username and password. These are used to authenticate ensuing api calls, and are not stored.


__See individual files for more detail__


If there's something that you think isn't obvious or is badly explained, let me (Colin) know

PAUL'S USE CASES

The scripts repo stores public scripts that everyone can read and learn from.
The staff repo stores private data that only teaching staff can read
  (like class lists, student e-mail addresses, etc.)

Many scripts are designed to be run from one directory up,
in the root where both "staff" and "scripts" are checked out.
I called this directory csf.org, because evergreen-csf is a Github org.
I also create a directory called "repos" where student repos are cloned and
pulled and graded.
 
It looks like this:

csf.org/
|
|-scripts/
|-staff/
|-repos/
  |
  |-aaabbb11
  |-cccddd22
  |-...

First I have to create "repos" and call

  python scripts/cloneAll.py

to initially clone all the student repos locally.
Colin uses list comprehensions, so you need Python 2.7 or later for this.

Then afterwards, when I want to pull updates, I call

  python scripts/pullAll.py

 
