from audioop import avg
inputFile = open("hw2.dat", "r")
outputFile = open("calculatedScores.dat", "w")

for line in inputFile:
    scores = line.split()
    name = scores[0]
    scores = [int(i) for i in scores[1:]]
    
    quizScores = scores[:3]
    hwScores = scores[3:8]
    examScores = scores[8:]
    
    quiz = sum(quizScores)/len(quizScores)
    hw = sum(hwScores)/len(hwScores)
    exam = sum(examScores)/len(examScores)
    
    finalScore = quiz * .2 + hw * .3 + exam * .5
    
    if finalScore > 90:
        letterGrade = 'A'
    elif finalScore > 80:
        letterGrade = 'B'
    elif finalScore > 70:
        letterGrade = 'C'
    elif finalScore > 60:
        letterGrade = 'D'
    else:
        letterGrade = 'F'
        
    outputFile.write("%20s %5.1f %1c\n" % (name, finalScore, letterGrade))
    