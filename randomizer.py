import random

# Ask the user for teams and the odds

home = raw_input("Who's the home team? ")
away = raw_input("Who are they playing against? ")
odds = raw_input("What are the odds for the home team? (Only enter the number, no %) ")

tokens = [] #Empty list to be filled from loops
homet = int(odds) 
awayt = 100 - int(odds)

#Add elements to the list for each team based on the odds

for i in range(homet):
    tokens.append("a")

for i in range(awayt):
    tokens.append("b")

result = random.choice(tokens)

if result == "a":
    print home +" will win"
elif result == "b":
    print away + " will win"
else: 
    print "Something went wrong, make sure to write the odds in digits only!"