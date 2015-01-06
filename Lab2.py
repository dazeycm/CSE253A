import random

#email address
emailAddress = str(input("Please enter an Email address: \n"))
nameAndDomain = emailAddress.split("@")
print("Your username is: {:s}\nYour domain is: {:s}".format(nameAndDomain[0], nameAndDomain[1]))

#create of short names
nameStr = str(input("Enter your full name separated with spaces: \n"))
nameParts = nameStr.split(" ")
if len(nameParts) < 3:
    shortName = nameParts[1][:6]
    shortName += nameParts[0][:1]
    
else:
    shortName = nameParts[2][:6]
    shortName += nameParts[0][:1]
    shortName += nameParts[1][:1]
     
print(shortName.lower())

#find number of 5's
randNums = []    
for x in list(range(0,10)):
    randNums.append(random.randint(1, 5))

print("There were a total of {:d} 5's".format(randNums.count(5)))

    
    

