#test.bash
vw -i iris.model -t -p ./predictions.txt < iris.test.vw
wc -l predictions.txt
comm -2 -3 <(sort iris.test.correct) <(sort predictions.txt) | wc -l
