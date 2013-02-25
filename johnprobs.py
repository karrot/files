import random

aceKing = 0
aceQueen = 0
tie = 0
cardRep = int(raw_input("Input repetitions: "))

for i in range(cardRep):
       r = random.randrange(10000)
       if (r+1 <= 423):
               tie += 1
       elif (r+1 <= 3084 and r+1 > 423):
               aceQueen += 1
       else:
               aceKing += 1

print "Tie:", tie
print "AQ: ", aceQueen
print "AK: ", aceKing
