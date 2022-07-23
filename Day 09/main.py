#Blind Auction
import auction_art
import os

def highest_bidder(bidding_record):
    highest=0
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if highest<bid_amount:
            winner=bidder
            highest=bid_amount
    print(f'The winner is {winner} with a bid of ${highest}')

print(auction_art.logo)
print("Welcome to the secret auction program")
bidder_list={}
other_bidders=True
while other_bidders:
    name=input("What is your name?")
    bidder_list[name]=int(input("What's your bid"))
    choice=input("Are there any othe bidders? Type yes or no").lower()
    if(choice=="no"):
        other_bidders=False
    else:
        os.system('clear')
highest_bidder(bidder_list)
