import random

inputFile = open('exam.dat')
nums = []
for line in inputFile:
    nums.append(int(line))
print(sum(nums))

nums.clear()
count = 0
for x in range(100):
    randNum = random.randrange(0, 101, 2)
    if randNum > 49:
        count += 1
    nums.append(randNum)
print(nums)
print('%d numbers greater than 49' % count)


date = input('Enter a date: ')
dateParts = []
if date.find('/') == -1:
    dateParts = date.split('-')
else:
    dateParts = date.split('/')
print('Month: %s\nDay: %s\nYear: %s\n' % (dateParts[0], dateParts[1], dateParts[2]))
