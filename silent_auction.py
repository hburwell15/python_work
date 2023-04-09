import os
from art_for_silent_auction import logo

print(logo)

print("Welcome to the secret auction program!\n")

auction_bids = {}

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}!")

keep_bidding = True
while keep_bidding:
  name = input("What is your name?\n")
  bid_price = int(input("How much would you like to bid? Please do not add any commas. \n$"))
  
  auction_bids[name] = bid_price
  print(auction_bids)

  more_bidders = input("Is there anyone else who would like to bid? Type 'yes' or 'no'.\n").lower()
  if more_bidders == "yes":
    os.system('clear')
  elif more_bidders == "no":
    keep_bidding = False
    find_highest_bidder(auction_bids)


#Another way to get the highest bidding amount
# highest_bidder = max(auction_bids, key=auction_bids.get)

# print(f"The winner is {highest_bidder} with a bid of {auction_bids[highest_bidder]}!")
  