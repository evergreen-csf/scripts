ALL_EVALS=~/src/csf.org/staff/data/14s/all-evals.txt

rm $ALL_EVALS

for file in *
	do echo $file
	echo "" "" "" >> $ALL_EVALS
	cd ~/src/csf.org/repos/$file
	echo $file >> $ALL_EVALS
	cat prog/*-words.txt >> $ALL_EVALS
	echo "" >> $ALL_EVALS
	cat sem/*-words.txt >> $ALL_EVALS
	echo "" >> $ALL_EVALS
	cat prog/*-credits.txt >> $ALL_EVALS
	echo "" >> $ALL_EVALS
	cat sem/*-credits.txt >> $ALL_EVALS
	echo "" >> $ALL_EVALS
done

