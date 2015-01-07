inputFile = open("hw2.dat", "r")
outputFile = open("calculatedScores.dat", "w")

for line in inputFile:
    scores = line.split()
    name = scores[0]
    scores = [int(i) for i in scores[1:]]
    
    quizScores = scores[:3]
    hwScores = scores[3:8]
    examScores = scores[8:]
    