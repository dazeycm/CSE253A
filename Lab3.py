import random

randNums = []
for i in list(range(1000)):
    randNums.append(random.randint(1, 10))
print("There were a total of %d 5's" % (randNums.count(5)))

dice = []
yahtzee = False
while(not yahtzee):
    for i in list(range(5)):
        dice.append(random.randint(1, 6))
    
    

