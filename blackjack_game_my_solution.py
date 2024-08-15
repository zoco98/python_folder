import os, random
"""casino says--
play blackjack
welcome winners"""
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

def draw_card():
    cards = list(card_dict.keys())
    card = random.choice(cards)
    cards.remove(card)
    return(card)

def sum(card_value):
    sum = 0
    for n in card_value:
        sum+=card_dict[n]
    return sum

dealer= [draw_card(), draw_card()]
player= [draw_card(), draw_card()]
print(f"Player: {player}, Dealer: {dealer}")

def player_hit(draw_card, sum, player):
    if sum(player)>reach:
        empty_dealer_player()
        print("player lose")
    else:
        player.append(draw_card())

def dealer_hit(draw_card_count, draw_card, dealer):
    dealer.append(draw_card())
    draw_card_count -= 1

def empty_dealer_player():
    dealer=[]
    player=[]

def stand(draw_card_count, reach, draw_card, sum, dealer, player, dealer_hit, empty_dealer_player):
    if sum(dealer)<reach:
        dealer_hit(draw_card_count, draw_card, dealer)
        print(f"Player: {player}, Dealer: {dealer}")
        if sum(dealer)>sum(player):
            empty_dealer_player()
            print("dealer win")
        elif sum(dealer)==sum(player):
            if sum(dealer)<reach:
                dealer_hit(draw_card_count, draw_card, dealer)
                print(f"Player: {player}, Dealer: {dealer}")
            else:
                print("it's draw")
        elif sum(dealer)<sum(player):
            empty_dealer_player()
            print("player win")
    elif sum(dealer)==reach:
        empty_dealer_player()
        print("dealer lose")

while draw_card_count>0:
    hit_stand = input("Want to draw card? hit/stand: ")
    if draw_card_count==0:
        print("game reached end point and it's show")
        print(f"Player: {player}, Dealer: {dealer}")
        if sum(player)<reach:
            dealer_hit(draw_card_count, draw_card, dealer)
        else:
            stand(draw_card_count, reach, draw_card, sum, dealer, player, dealer_hit, empty_dealer_player)
    else:
        if hit_stand=="hit":
            player_hit(draw_card, sum, player)
            print(f"Player: {player}, Dealer: {dealer}")
        elif hit_stand=="stand":
            stand(draw_card_count, reach, draw_card, sum, dealer, player, dealer_hit, empty_dealer_player)


    
    