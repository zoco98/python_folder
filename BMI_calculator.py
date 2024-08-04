weight = float(input("enter weight in KG: \n"))
height = float(input("enter height in meter: \n"))

bmi = weight / (height**2)
rounded_bmi = round(bmi,2)
print("your BMI: "+ str(bmi))
print("your BMI: "+ str(round(bmi,2)))
#f-string
print(f"your BMI: {rounded_bmi}")

# Enter your height in meters e.g., 1.55
height = float(input("enter weight in KG: \n"))
# Enter your weight in kilograms e.g., 72
weight = int(input("enter height in meter: \n"))
bmi = float(weight)/(height**2)
if bmi<18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi>=18.5 and bmi<25.0:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi>=25.0 and bmi<30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi>=30.0 and bmi<35.0:
  print(f"Your BMI is {bmi}, you are obese.")
elif bmi>=35.0:
  print(f"Your BMI is {bmi}, you are clinically obese.")
