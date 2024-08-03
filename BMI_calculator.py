weight = float(input("enter weight in KG: \n"))
height = float(input("enter height in meter: \n"))

bmi = weight / (height**2)
rounded_bmi = round(bmi,2)
print("your BMI: "+ str(bmi))
print("your BMI: "+ str(round(bmi,2)))
#f-string
print(f"your BMI: {rounded_bmi}")