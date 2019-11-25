import order_processor
import brand_factories


class GarmentMaker:
    """
    driver class that creates 3 arrays to store the garments
    determines garment type, and calls the correct factory to
    create order.count number of items and append to list
    """

    def __init__(self, order):
        """
        creates 3 lists to hold different type of garments
        :param order: order of garments from order_processor.py
        """
        self.shirts_men = []
        self.shirts_women = []
        self.socks_unisex = []
        self.order = order

    def determine_garment(self, order):
        """
        looks into the order to determine which garment is
        being ordered, then sends it to the correct method
        :param order: order of garments from order_processor.py
        :return:
        """
        if order.garment == "ShirtMen":
            self.shirt_men_maker(order)
        elif order.garment == "ShirtWomen":
            self.shirt_women_maker(order)
        else:
            self.socks_unisex_maker(order)

    def shirt_men_maker(self, shirt_men_order):
        """
        sends a creation request for a ShirtMen object,
        the other two do the same for ShirtWomen and SockPairUnisex objects
        :param shirt_men_order: Order of garments from order_processor.py
        :return:
        """
        self.shirts_men.extend([shirt_men_order.factory.create_shirt_men(shirt_men_order)] * shirt_men_order.count)

    def shirt_women_maker(self, shirt_women_order):
        self.shirts_women.extend([shirt_women_order.factory.create_shirt_men(shirt_women_order)] *
                                 shirt_women_order.count)

    def socks_unisex_maker(self, socks_unisex_order):
        self.shirts_men.extend([socks_unisex_order.factory.create_shirt_men(socks_unisex_order)] *
                               socks_unisex_order.count)