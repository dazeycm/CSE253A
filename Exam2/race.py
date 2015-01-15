inputFile = open('exam2.dat', 'r')
stats = {}

def formatTime(time):
    minutes = time // 60
    seconds = time % 60
    if len(str(seconds)) < 2:
        seconds = str(seconds) + '0' 
    return str(minutes) + ":" + str(seconds)

for line in inputFile:
    parts = line.split()
    name = parts[0]
    timeParts = parts[1].split(':')
    time = int(timeParts[0]) * 60 + int(timeParts[1])
    if time in stats:
        stats[time].append(name)
    else:
        stats[time] = []
        stats[time].append(name)

times = sorted(list(stats))
    
for time in times:
    nameList = ''
    for name in stats[time]:
        nameList += name + ' '
        
    print('%s %s' % (formatTime(time), nameList))


    