import os
#declaring functions
def add(n1, n2):
    return n1+n2
def substract(n1, n2):
    return n1-n2
def multiply(n1, n2):
    return n1*n2
def divide(n1, n2):
    if n2!=0:
        return n1/n2
    else:
        print("infinte")
  
end_game=True
while end_game:
    os.system('cls')
    #taking inputs
    number_first = int(input("Enter 1st number:\n"))
    number_second = int(input("Enter 2nd number:\n"))
    opr = input(" +,\n -,\n *,\n /\nchoose operation:")  
    switch={
            '+' : add(n1=number_first, n2=number_second),
            '-' : substract(n1=number_first, n2=number_second),
            '*' : multiply(n1=number_first, n2=number_second),
            '/' : divide(n1=number_first, n2=number_second)
        }
    end_result = switch.get(opr)
    print(f"{number_first} {opr} {number_second} : {end_result}")
    ch = input("do you want to continue? yes/no? \n")
    if ch=="no":
        end_game=False
    