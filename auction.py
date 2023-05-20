from auctionArt import logo

print(logo)
print("Welcome to the secret auction program!!!")

endGame = False
auction = {}

while not endGame:
    name = input('What is your name: ')
    bid = int(input('What is your bid: '))
    auction[name] = bid

    status = input("Are there any other bidders? Type 'yes' or 'no': ")

    if status == 'no':
        endGame = True
        maxBidder = 'nobody'
        maxBid = 0
        for i in auction:
            if auction[i] > maxBid:
                maxBid = auction[i]
                maxBidder = i
        print(f"The winner is {maxBidder} with a bid of {maxBid}$")


