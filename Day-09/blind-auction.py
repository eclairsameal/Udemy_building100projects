from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.
print(art.logo)
print("Welcome to tho secret auction program.")

def find_highest_bid(bid_list):
    highest_bid = 0
    highest_bidder = ""

    for bid_dict in bid_list:
        if bid_dict["bid"] > highest_bid:
            highest_bid = bid_dict["bid"]
            highest_bidder = bid_dict["name"]
    print(f"The highest bidder is {highest_bidder} with a bid of ${highest_bid}. ")

bid_list = []
auction_flag = False
while not auction_flag:
    name = input("What is you name?:")
    bid = int(input("What's your bid?: $"))
    bid_list.append({"name": name,"bid":bid})

    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if other_bidders == 'no':
        auction_flag = True
    else:
        clear()
find_highest_bid(bid_list)
