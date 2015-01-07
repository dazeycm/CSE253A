import math

stats = str(input("Enter QB stats in order of games, attempts, completions, yards, interceptions, and touchdowns: "))
stats = stats.split()

error = False

for stat in stats:
    if not stat.isnumeric():
        error = True
        
if not error:        
    games = int(stats[0])
    attempts = int(stats[1])
    completions = int(stats[2])
    yards = int(stats[3])
    interceptions = int(stats[4])
    touchdowns = int(stats[5])
    
    if games < 0 or games > 16: 
        error = True;
    if attempts < 0:
        error = True;
    if completions < 0 or completions > attempts:
        error = True;
    if yards < -99 * completions or yards > 99 * completions:
        error = True;
    if interceptions < 0 or interceptions > attempts - completions:
        error = True;
    if touchdowns < 0 or touchdowns > completions:
        error = True;

if not error:
    completionPerc = ((completions/attempts) - .3) * 5
    touchdownPerc = (touchdowns / attempts) * 20
    yardsPerAttempt = ((yards / attempts) - 3) * .25
    interceptionPerc = 2.375 - (interceptions / (4 * attempts) * 100)
    
    if completionPerc < 0:
        completionPerc = 0
    if completionPerc > 2.375:
        completionPerc = 2.375
    if touchdownPerc < 0:
        touchdownPerc = 0
    if touchdownPerc > 2.375:
        touchdownPerc = 2.375
    if yardsPerAttempt < 0:
        yardsPerAttempt = 0
    if yardsPerAttempt > 2.375:
        yardsPerAttempt = 2.375
    if interceptionPerc < 0:
        interceptionPerc = 0
    if interceptionPerc > 2.375:
        interceptionPerc = 2.375
    
    rating = ((completionPerc + touchdownPerc + yardsPerAttempt + interceptionPerc) / 6) * 100
    
    roundRating = rating % 1
    
    if roundRating >= .5:
        rating = math.ceil(rating)
    else:
        rating = math.floor(rating)
    
    print("QB rating is: " + str(rating))
    
    if rating >= 110:
        if games >= 10:
            print("Hall of Fame")
        else:
            print("Stellar")
    elif rating >= 90 and rating < 110:
        print("Impressive")
    elif rating >= 70 and rating < 90:
        print("Decent")
    elif rating < 70:
        print("Dismal")
else: 
    print("There was an error with your input!")