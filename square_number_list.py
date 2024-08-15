numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

def squared_number(params):
  return params*params
  
squared_numbers=[]
for n in numbers:
  squared_numbers.append(squared_number(params=n))
print(squared_numbers)
