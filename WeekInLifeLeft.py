age = int(input("Enter your age: \n"))
LIFT_TIME = 90
rest_age_left = LIFT_TIME - age
week_left = rest_age_left * 52
print(f"You have {week_left} weeks left.")