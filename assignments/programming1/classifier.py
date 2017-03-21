"""

    Samuel Cuthbertson

    sacu2067

    samuel.cuthbertson@colorado.edu

    Code for Iris Naive Bayes Classifier

"""
import sys, csv, math
from collections import defaultdict

def dumpclean(obj):
    for k in range(1,4):
        for j in range(0,len(obj[k])):
            print(obj[k][j][0], obj[k][j][1], obj[k][j][2], obj[k][j][3])

data_matrix = defaultdict(lambda:defaultdict(lambda:defaultdict(float)))

with open("iris.train", newline="") as trainfile:
    datareader = csv.reader(trainfile, delimiter=',')
    counter = [0,0,0,0]
    for row in datareader:
        data_matrix[int(row[0])][counter[int(row[0])]][0] = row[1]
        data_matrix[int(row[0])][counter[int(row[0])]][1] = row[2]
        data_matrix[int(row[0])][counter[int(row[0])]][2] = row[3]
        data_matrix[int(row[0])][counter[int(row[0])]][3] = row[4]
        counter[int(row[0])]+=1



with open("iris.test", newline="") as testfile:
    datareader = csv.reader(testfile, delimiter=',')

    correct = 0
    wrong = 0

    correctconfidence = 0;
    wrongconfidence = 0;

    for row in datareader:
        correctclass = int(row[0])
        p_row_given_class = [-1,0,0,0]

        for h in range(1,4): # Which class?
            logprob = math.log(1/3) # Log prob w/ Maximum Likelihood
            for i in range(0,4): # Which feature?
                k = i+1
                count = 0
                occurences = 1 # Laplace Smoothing
                for j in range(0,len(data_matrix[h])):
                    if data_matrix[h][j][i] == row[k]:
                        occurences += 1
                    count += 1
                logprob += math.log(occurences/count)
            p_row_given_class[h] = math.exp(logprob)

        bestclass = 0
        probofbestclass = 0
        for h in range(1,4):
            p_class_given_row = p_row_given_class[h]
            denominator = 0
            for i in range(1,4):
                denominator += p_row_given_class[i]
            p_class_given_row = math.exp(math.log(p_class_given_row) - math.log(denominator))
            if p_class_given_row > probofbestclass:
                bestclass = h
                probofbestclass = p_class_given_row

        if bestclass == correctclass:
            correct += 1
            correctconfidence += probofbestclass
        else:
            wrong += 1
            wrongconfidence += probofbestclass

    percentage = (correct / (correct + wrong))*100

    print("Average Probability on Correct Classifications: ",
            correctconfidence/correct)
    print("Average Probability on Incorrect Classifications: ",
            wrongconfidence/wrong)
    print("Percent correct: ", percentage)
