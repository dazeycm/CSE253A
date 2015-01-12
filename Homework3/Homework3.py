#dictionary where key is state code and value is list
#set for entities
#to get number of states an entity is in
#   Go through set and see if it is in a value in the dictionary

# for timezone stuff, key is time zone, value = list of states

#returns the key with the max value in a dictionary
def keyWithMaxValue(dict):
    vals = list(dict.values())
    keys = list(dict.keys())
    return keys[vals.index(max(vals))]

def keyWithMaxValueL(dict):
    vals = list(dict.values())
    vals = [len(miniList) for miniList in vals]
    keys = list(dict.keys())
    return keys[vals.index(max(vals))]

inputFile = open('US.dat', 'r')

sanityCount = 0
uniqueEntityNames = set()
entityCount = {}
stateEntityCount = {}
entityStateCount = {}

for line in inputFile:
    sanityCount += 1
    print(sanityCount)
    
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
    
print('Number of unique entities: %d' % len(uniqueEntityNames))

key = keyWithMaxValue(entityCount)
print('Entity with the most appearences: %s\nNumber of appearences: %d' % (key, entityCount[key])) 
for state in stateEntityCount:
    print('%s: %d' % (state, len(stateEntityCount[state])))

print()
stateEntityList = sorted(stateEntityCount)
for state in stateEntityList:
    print('%s: %d' % (state, len(stateEntityCount[state])))

entity = keyWithMaxValueL(entityStateCount)
print(entity)
print(len(entityStateCount[entity]))







