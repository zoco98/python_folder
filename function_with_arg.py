def life_in_weeks(current_age):
    total_life_time = 90
    leftover_life_time = total_life_time - current_age
    leftover_life_time_in_weeks = leftover_life_time*52
    print(f"You have {leftover_life_time_in_weeks} weeks left")
    
age = int(input())
life_in_weeks(age)
    
def calculate_love_score(male, female):
    scale = "truelove"
    couple = male+female
    print(couple)
    love_score = 0
    for letter in scale:
        love_score+=couple.count(letter)
    print(love_score)
        
calculate_love_score(male = "Kanye West", female="Kim Kardashian")

def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)

#none--output--this will not give any error just it not gonna print any output
def my_function(a):
    if a < 40:
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25))