#1.
"""
def numInList(number, list):
    return list.count(number)
"""
import functools
f = lambda number, list: list.count(number)

#2.
a = [i % 2 for i in range(11)]
print(a)
b = [2 ** i for i in range(11)]
print(b)
c = [[1 if j <= i else 0 for j in range(4)] for i in range(4)]
print(c)

#3. 2500000 3500000 5500000

#4. 
l = list(range(1, 10))
u = ['craig@dazey', 'ben@gmail.com', 'hello@world.comc']
print(list(map(lambda x : -x, l)))
print(list(map(lambda x : x % 2 == 0, l)))
print(list(map(lambda x : x.split('@')[0], u)))

#5.
print(functools.reduce(lambda x,y : x * y, l))

#6.
popOfAllStates = {'OH':2300000, 'MI':4000000, 'KY':2500000, 'IN':3500000, 'IL':5500000 }
print(list(filter(lambda x : popOfAllStates[x] >= 3000000, popOfAllStates)))





