import art

print(art.logo)


def highest_bid(bid_money):
    highest_money = 0
    winner = ""
    for people in bid_money:
        bid_amount = bid_money[people]
        if bid_amount > highest_money:
            highest_money = bid_amount
            winner = people

    print(f"The winner is {winner} with total bid of {highest_money} ")


bidders = {}
still_bidding = True
while still_bidding:
    bidder_name = input("Enter Your Name:")
    bidder_price = int(input("Enter Your bid:"))
    bidders[bidder_name] = bidder_price
    should_continue = input("Are there more bidders?")
    if should_continue == "yes":
        print("\n" * 30)

    elif should_continue == "no":
        highest_bid(bid_money=bidders)
        still_bidding = False

    else:
        print("Type yes or no")