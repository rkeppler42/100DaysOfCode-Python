import art


print(art.logo)

name = input("What is your name?:  ")
bid = float(input("What is your bid?:  $"))
user_input = input("Are there any other bidders? Type 'yes' or 'no'.\n")
bidders = {name: bid}

while user_input == "yes":
    name = input("What is your name?:  ")
    bid = float(input("What is your bid?:  $"))
    bidders[name] = bid
    user_input = input("Are there any other bidders? Type 'yes' or 'no'.\n")

max_bid = 0
max_bidder = ""

for name in bidders:
    if bidders[name] > max_bid:
        max_bid = bidders[name]
        max_bidder = name

print(f"The winner is {max_bidder} with a bid of ${max_bid:.2f}.")