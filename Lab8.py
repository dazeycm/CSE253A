import random
import statistics
import datetime
import shutil
import os.path

def shuffleCards():
    cards = []
    card = 0
    color = 0
    for i in range(52): 
        card = card % 13
        color = color % 4
        card += 1
        color += 1
        cards.append((card, color))
    
    random.shuffle(cards)
    print(cards)

#statistics.median will take the mean of the middle two elements
#there is also median_low and median_high which will return the lower
#and higher number of the middle two numbers respectively
def meanAndStDev():
    nums = []
    for i in range(1000):
        nums.append(random.triangular(10, 18, 20))
        
    mean = statistics.mean(nums)
    stdv = statistics.stdev(nums, mean)
    print(mean, stdv)
#the statistics library throws a StatisticsError exception

def dateOfThanksGiving(year):
    numTh = 0
    day = 1
    if not str(year).isdigit() or year < 0:
        return None
    else:
        for i in range(50):
            if datetime.date(year, 11, day).weekday() == 3:
                numTh += 1
                if numTh == 4:
                    return '11-%d-%d' % (day, year)
            day += 1

def copy(source, destination):
    for file in os.listdir(source):
        filePath = os.path.join(source, file)
        destPath = os.path.join(destination, file)
        shutil.copy(filePath, destPath)

shuffleCards()
meanAndStDev()
print(dateOfThanksGiving(2020))
copy(r'C:\Users\dazeycm\Desktop\test', r'C:\Users\dazeycm\Desktop\test1')

