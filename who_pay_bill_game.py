import random

#introducing list data structure
#who pays the bill game
names=["Angela", "Ben", "Jenny", "Michael", "Chloe"]
random = random.randint(0,len(names)-1)
random_person = names[random]
print(f"{random_person} is going to buy the meal today!")

print(f"{names[0]} , {names[1]} , {names[-1]} , {names[-2]}")