import os
#taking inputs
your_name = input("what's your name: \n")
start_bidding_amount = int(input("How much you want to bid: \n"))

#declare var
bid_dict = {}
max_bid = 0
winner = ""
bid_dict[your_name] = start_bidding_amount

auction_closed = False
while not auction_closed:
    #taking inputs
    bidder_count = input("is there anymore bidder? yes/no: \n")
    if bidder_count == "yes":
        #clear console after each bid
        #print("\n"*100)
        os.system('cls')
        bidder_name = input("what's bidder name: \n")
        bidder_amount = int(input("How much you want to bid: \n"))
        bid_dict[bidder_name] = bidder_amount
    else:
        auction_closed = True

#print(bid_dict)
os.system('cls')
print("\n*************winner*************\n")
print("method-1: looping with max var")
for key in bid_dict:
    if bid_dict[key]>max_bid:
        winner = key
        max_bid = bid_dict[key]
print(f"Winner is {winner} who bid for {max_bid}")
print("\n*************winner*************\n")

print("\n*************winner*************\n")
print("method-2: using max function")
max(bid_dict,key=bid_dict.get)
print(f"Winner is {winner} who bid for {max_bid}")
print("\n*************winner*************\n")


