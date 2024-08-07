import random

word_list = ["orange","mango","guava","watermelon","grapes"]
guess_list = []
placeholder = ""
game_over = False

random_word = random.choice(word_list)
word_length = len(random_word)
user_life = word_length

for n in range(0,word_length):
    placeholder+="_"
print(placeholder)

while not game_over and user_life>0:
    guess = input(f"guess a letter: ").lower()
    display=""
    for letter in random_word:
        if letter == guess:
            display+=guess
            guess_list.append(guess)
            user_life +=1 
        elif letter in guess_list:
            display+=letter
        else:
            display+="_"
    user_life-=1
    print(f"{display} -- user life: {user_life}")
    if "_" not in display:
        game_over = True
        print("you win !!!")

if user_life==0 and not game_over:
    print("you loser!!!")
    print(random_word)
    
    

