#! /bin/bash

curdir=$(pwd)
for student in *
	do echo $student
	if [ ! -e $student/arch/hw3 ]; then
		continue
	fi
	cd $student/arch/hw3
	jasmin Count5.j > grade.log 2>&1
	jasmin LeapYear.j >> grade.log 2>&1
   	lc=$(cat grade.log | wc -l)
	echo $lc
	if [ $lc -eq 0 ]; then
		echo $student " PASSES";
   	fi
	cd $curdir
done

echo "Done!"

