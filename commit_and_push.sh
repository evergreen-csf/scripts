for file in *; do echo $file; cd ~/src/csf.org/repos/$file; git add prog/*.txt sem/*.txt; git commit -a -m "First pass at generating evaluations and credits."; git push origin master; done
