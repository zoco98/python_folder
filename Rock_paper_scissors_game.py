import random

#rock paper scissors game
print('''
      **rock**      ====== *1*
      **paper**     ====== *2*
      **scissors**  ====== *3*
''')
game = ["rock","paper","scissors"]

human_choice = int(input("1/2/3? "))-1
computer_choice = random.randint(0,len(game)-1)
print(f"you: {game[human_choice]} \ncomputer: {game[computer_choice]}")

if human_choice == computer_choice:
    print("its a draw!")
elif human_choice==2 and computer_choice==0:
    print("!!!!you lose!!!!")
elif human_choice==0 and computer_choice==2:
    print("****you win****")
elif human_choice>computer_choice:
    print("****you win****")
elif human_choice<computer_choice:
    print("!!!!you lose!!!!")
else:
  print("invalid choice")