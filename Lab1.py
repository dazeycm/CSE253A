import math

leg1 = int(input("Enter leg1: "))
leg2 = int(input("Enter leg2: "))
hypot = math.sqrt((leg1**2) + (leg2**2))
print(hypot)

fenceLen = int(input("Enter fence length: "))
sectionLen = 10
sections = math.ceil(fenceLen/10)
print(sections)

print(math.sin(math.radians(0)))
print(math.sin(math.radians(25)))
print(math.sin(math.radians(30)))
print(math.sin(math.radians(60)))
print(math.sin(math.radians(75)))
print(math.sin(math.radians(90)))

quiz = int(input("Enter quiz average: "))
homework = int(input("Enter homework average: "))
exam = int(input("Enter exam average: "))

quizWeight = .2
homeworkWeight = .3
examWeight = .5

score = (quiz * quizWeight) + (homework * homeworkWeight) + (exam * examWeight)
print(score)
 
if score > 90:
	print("A")
elif score > 80:
	print("B")
elif score > 70:
	print("C")
elif score > 60:
	print("D")
else:
	print("F")
	
year = int(input("Enter year: "))
isLeapYear = False
if (year % 4 == 0) and (year % 100 != 0):
	isLeapYear = True;
elif (year % 100 == 0) and (year % 400 == 0):
	isLeapYear = True;
print(isLeapYear)
