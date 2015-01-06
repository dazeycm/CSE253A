import random

randNums = []
for i in list(range(1000)):
    randNums.append(random.randint(1, 10))
print("There were a total of %d 5's" % (randNums.count(5)))

count = 0
while True:
    dice = []
    for i in list(range(5)):
        dice.append(random.randint(1, 6))
    count += 1
    if dice[0] == dice[1] == dice[2] == dice[3] == dice[4]:
        break
print("Got yahtzee on the %dth try" % (count))

for x in range(1000000):
    dice = []
    for i in list(range(5)):
        dice.append(random.randint(1,6))
    if dice[0] == dice[1] == dice[2] == dice[3] == dice[4]:
        count += 1
print(count/1000000)

inputFile = open("weather.dat", "r")
outputFile = open("stats.dat", "w")
for line in inputFile:
    data = line.split()
    #list comprehensions: https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions
    data = [float(i) for i in data]
    outputFile.write("Mininum: %.0f    Maximum: %.0f\n" % (min(data), max(data)))

        




    

