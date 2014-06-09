. scripts/reset_credit_files.sh 
cd ..
for file in repos/*; do echo $file; python scripts/generate_eval_text.py "${file/repos\/}"; done
