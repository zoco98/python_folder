import os, random
print('''
    \n*****************the casino says welcome*****************\n''')
card_dict={
    "1" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "king" : 10,
    "queen" : 10,
    "jack" : 10,
    "Ace" : 11
}

draw_card_count = 2
reach = 21
end_game=False
def draw_card():
    cards = list(card_dict.keys())
    card = random.choice(cards)
    cards.remove(card)
    return(card)

def sum(card_value):
    sum = 0
    for n in card_value:
        sum+=card_dict[n]
    if sum == reach and "Ace" in card_value:
        sum = sum - 10
    return sum

player= [draw_card(),draw_card()]
dealer= [draw_card(),draw_card()]
print(f"Player: {player}")

def player_hit(draw_card, sum, player, draw_card_count):
    player.append(draw_card())
    draw_card_count -= 1
    print(f"Player: {player}")
    if sum(player)>reach:
        print("player lose")
        empty_dealer_player()
    elif sum(player)==reach:
        print("player win")
        empty_dealer_player()
        

def dealer_hit(draw_card_count, draw_card, dealer):
    dealer.append(draw_card())
    print(f"Dealer: {dealer}")
    if sum(dealer)>reach:
        print("dealer lose")
        empty_dealer_player()
    elif sum(player)==reach:
        print("dealer win")
        empty_dealer_player()
    draw_card_count -= 1

def empty_dealer_player():
    print(f"Player: {player}, Dealer: {dealer}")
    dealer.clear()
    player.clear()
    draw_card_count = 2

def stand(draw_card_count, reach, draw_card, sum, dealer, player, dealer_hit, empty_dealer_player):
    if sum(dealer)<reach:
        dealer_hit(draw_card_count, draw_card, dealer)
        if sum(dealer)>sum(player):
            print("dealer win")
            empty_dealer_player()
        elif sum(dealer)==sum(player) and sum(player) != 0 and sum(dealer) != 0:
            if sum(dealer)<reach:
                dealer_hit(draw_card_count, draw_card, dealer)
            else:
                print("it's draw")
        elif sum(dealer)<sum(player):
            print("player win")
            empty_dealer_player()
    elif sum(dealer)==reach:
        print("dealer lose")
        empty_dealer_player()

while not end_game:
    hit_stand = input("Want to draw card? hit/stand: ")
    if draw_card_count==0:
        print("game reached end point and it's show")
        print(f"Player: {player}, Dealer: {dealer}")
        if sum(player)<reach:
            dealer_hit(draw_card_count, draw_card, dealer)
        else:
            stand(draw_card_count, reach, draw_card, sum, dealer, player, dealer_hit, empty_dealer_player)
    elif sum(player) != 0 and sum(dealer) != 0:
        if hit_stand=="hit":
            player_hit(draw_card, sum, player, draw_card_count)
        elif hit_stand=="stand":
            stand(draw_card_count, reach, draw_card, sum, dealer, player, dealer_hit, empty_dealer_player)
        else:
            end_game=True

    else:
        player_hit(draw_card, sum, player, draw_card_count)
        player_hit(draw_card, sum, player, draw_card_count)
        dealer_hit(draw_card_count, draw_card, dealer)
        dealer_hit(draw_card_count, draw_card, dealer)

    
    