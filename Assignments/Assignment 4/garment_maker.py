import order_processor
import brand_factories


class GarmentMaker:

    def __init__(self, order):
        self.shirts_men = []
        self.shirts_women = []
        self.socks_unisex = []
        self.order = order

    def determine_garment(self, order):
        if order.garment == "ShirtMen":
            self.shirt_men_maker(order)
        elif order.garment == "ShirtWomen":
            self.shirt_women_maker(order)
        else:
            self.socks_unisex_maker(order)

    def shirt_men_maker(self, shirt_men_order):
        shirt_men_order.factory.create_shirt_men()

    def shirt_women_maker(self, shirt_women_order):
        shirt_women_order.factory.create_shirt_women()

    def socks_unisex_maker(self, socks_unisex_order):
        socks_unisex_order.factory.create_socks_unisex()