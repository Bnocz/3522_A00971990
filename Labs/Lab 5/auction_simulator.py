import random
class Bidder:

    def __init__(self, name, budget, bid_probability,
                 bid_increase_perc, highest_bid):
        self.name = name
        self.budget = budget
        self.bid_probability = bid_probability
        self.highest_bid = 0
        self.bid_increase_perc = bid_increase_perc


    def bid(self, auctioneer):
        bid = auctioneer.highest_current_bid * self.bid_increase_perc
        if bid <= self.budget:
            return bid
        elif bid >= self.budget:
            return self.budget

    def __call__(self, auctioneer):
        bid_chance = random.random()
        if bid_chance < self.bid_probability:
            auctioneer.check_bid(self.name)
        else:
            pass


class Auctioneer:

    def __init__(self):
        self.highest_current_bid = None
        self.highest_current_bidder = None
        self.bidder_list = []

    def check_bid(self, name):
        if name is not self.highest_current_bidder:
            bid = name.bid
            if bid > self.highest_current_bid:
                self.highest_current_bid = bid
                self.highest_current_bidder = name
                self.execute_callbacks()
                return True
            else:
                return False
        else:
            return False

    def attach_bidder(self, callback):
        self.bidder_list.append(callback)

    def execute_callbacks(self):
        for bidder in self.bidder_list:
            bidder(self)


class Auction:

    def __init__(self, bidders, item, starting_price):