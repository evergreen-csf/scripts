#! /bin/bash
# Resets (erases) generated eval words and credit files.

cd repos

for file in *
	do echo $file
	rm $file/{prog,sem}/$file-credits.txt
	rm $file/{prog,sem}/$file-words.txt
done