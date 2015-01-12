#returns the key with the max value in a dictionary
def keyWithMaxValue(dict):
    vals = list(dict.values())
    keys = list(dict.keys())
    return keys[vals.index(max(vals))]

#returns the key with max value in a dictionary, where the value is a list
def keyWithMaxValueL(dict):
    vals = list(dict.values())
    vals = [len(miniList) for miniList in vals]
    keys = list(dict.keys())
    return keys[vals.index(max(vals))]

inputFile = open('US.dat', 'r')

uniqueEntityNames = set()   #set of unique entities
entityCount = {}            #dict to count the occurence of each entity
stateEntityCount = {}       #dict where state is key, list of entity is value
entityStateCount = {}       #dict where entity is key, set of states is value
timeZoneEntityCount = {}    #dict where timezone is key, list of entities is value

for line in inputFile:
    line = line.split('\t')
    entity = line[0]
    state = line[1]
    timeZone = line[4]
    
    uniqueEntityNames.add(entity)
    
    if entity not in entityCount:
        entityCount[entity] = 1
    else: 
        entityCount[entity] += 1
    
    if state in stateEntityCount:
        stateEntityCount[state].append(entity)
    else:
        stateEntityCount[state] = []
        stateEntityCount[state].append(state)
    
    if entity in entityStateCount:
        entityStateCount[entity].add(state)
    else:
        entityStateCount[entity] = set()
        entityStateCount[entity].add(state)
        
    if timeZone in timeZoneEntityCount:
        timeZoneEntityCount[timeZone].append(entity)
    else:
        timeZoneEntityCount[timeZone] = []
        timeZoneEntityCount[timeZone].append(entity)

#Print number of unique entities    
print('Number of unique entities: %d' % len(uniqueEntityNames))

#Prints the entity name that appears most in the file
key = keyWithMaxValue(entityCount)
print('Entity with the most appearences: %s\nNumber of appearences: %d' % (key, entityCount[key]))

#Prints each state and the number of entities in that state
for state in stateEntityCount:
    print('%s: %d' % (state, len(stateEntityCount[state])))

#Prints the state and the number of entities in that state, ordered by state abbreviation
print()
stateEntityList = sorted(stateEntityCount)
for state in stateEntityList:
    print('%s: %d' % (state, len(stateEntityCount[state])))

#Prints the entity name that appears in the most states
entity = keyWithMaxValueL(entityStateCount)
print('Entity that appears in the most states: %s' % entity)

#Prints the time zone that contains the most entities
timeZone = keyWithMaxValueL(timeZoneEntityCount)
print('Time Zone with the most entities: %s' % timeZone)







