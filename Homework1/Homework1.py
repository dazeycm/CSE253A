import math

games = int(input("Number of games: "))
attempts = int(input("Number of attempts: "))
completions = int(input("Number of completions: "))
yards = int(input("Number of yards: "))
interceptions = int(input("Number of interceptions: "))
touchdowns = int(input("Number of touchdowns: "))

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
