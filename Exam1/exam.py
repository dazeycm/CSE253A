import random

inputFile = open('exam.dat')
nums = []
for line in inputFile:
    nums.append(int(line))
print(sum(nums)/len(nums))

nums.clear()
count = 0
for x in range(100):
    randNum = random.randrange(0, 101, 2)
    if randNum > 49:
        count += 1
    nums.append(randNum)
print(nums)
print(count)

#===============================================================================
# date = input('Enter a date: ')
# dateParts = []
# if date.find('/') == -1:
#     dateParts = date.split('-')
# else:
#     dateParts = date.split('/')
# print('Month: %s\nDay: %s\nYear: %s\n' % (dateParts[0], dateParts[1], dateParts[2]))
#===============================================================================

date = input('Enter a date: ')
month = date[0:2]
day = date[3]
year = date[5:]
print('Month: %s\nDay: %s\nYear: %s\n' % (month, day, year))