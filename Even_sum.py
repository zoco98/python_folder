target = int(input("enter range: ")) 
even_sum=0
for n in range(1, target+1):
  if n%2 == 0:
    even_sum +=n

print(even_sum)