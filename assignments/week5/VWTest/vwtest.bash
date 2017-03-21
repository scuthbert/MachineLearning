#test.bash
vw -i vw.model -t -p ./predictions.txt < test
wc -l predictions.txt
comm -2 -3 <(sort test.answers) <(sort predictions.txt) | wc -l

