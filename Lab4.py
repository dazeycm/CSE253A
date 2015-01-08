import math

def caloriesBurnedRunning(weight, distance):
    return .75 * pounds * distance

def hypotenuse(leg1, leg2):
    return math.sqrt(math.pow(leg1, 2) + math.pow(leg2, 2))

def normalizeAngle(angle):
    return angle % 360

def identityMatrix(N):
    return [[0 if x != y else 1 for x in range(N)] for y in range(N)]

def convertToFloatArray(str):
    return [float(i) for i in str.split()]

def pieChart(values):
    return [i/sum(values) for i in values]