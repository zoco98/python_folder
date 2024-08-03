weight = float(input("enter weight in KG: \n"))
height = float(input("enter height in meter: \n"))

bmi = weight / (height**2)
print("your BMI: "+ str(bmi))