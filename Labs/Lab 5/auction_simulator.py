class Bidder:

    def __init__(self, name, budget, bid_probability, bid_increase_perc, highest_bid)
        self.name = name
        self.budget = budget
        self.bid_probability = bid_probability
        self.highest_bid = highest_bid
        self.bid_increase_perc = bid_increase_perc

    def __call__(self, auctioneer):
        print(f"Hi, I'm a bidder, my name is {self.name}")


class Auctioneer:

    def __init__(self)
        self.highest_current_bid = None
        self.highest_current_bidder = None
        bidder_list = []


class Auction:

    def __init__(self, bidders, item, starting_price):