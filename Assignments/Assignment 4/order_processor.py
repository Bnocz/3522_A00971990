import pandas
import brand_factories


class OrderProcessor:
    """
    Class that processes orders from an excel file using pandas
    has methods to read, then process row by row.
    """
    def __init__(self, file_path):
        """
        initializes order processor with a file path and
        current order
        :param file_path: the path of the excel file
        """
        self.file_path = "COMP_3522_A4_orders.xlsx"
        self.order = None

    def read_order(self):
        """
        opens and reads an excel sheet using pandas
        """
        self.order = pandas.read_excel(self.file_path)
        return self.order

    def process_order(self, index_):
        """
        locates a row by its integer index, and assigns that row to a variable
        has if checks for the brand and assigns factory variable to the correct
        factory. Packages both row and factory into an object of type Order and
        returns it.
        :param index_:
        :return:
        """
        row_ = self.order.iloc[index_]
        factory = None
        if row_["Brand"] == "Lululime":
            factory = brand_factories.LuluLimeFactory()
        if row_.Brand == "PineappleRepublic":
            factory = brand_factories.PineAppleRepublicFactory()
        if row_.Brand == "Nika":
            factory = brand_factories.NikaFactory()

        return Order(row_, factory)


class Order:
    """
    contains information about customer orders. Is used in garment_maker
    to help the factories create the needed order
    """

    def __init__(self, row, factory):
        self.row = row
        self.factory = factory
        self.garment = row["Garment"]
        self.count = row["Count"]
        self.style_name = row["Style Name"]
        self.size = row["Size"]
        self.Colour = row["Colour"]
        self.textile = row["Textile"]
        self.sport = row["Sport"]
        self.hidden_zipper = row["Hidden Zipper Pockets"]
        self.requires_dry_cleaning = row["Dry Cleaning"]
        self.category = row["Indoor/Outdoor"]
        self.no_iron = row["Requires Ironing"]
        self.buttons = row["Buttons"]
        self.is_articulated = row["Articulated"]
        self.sock_length = row["Length"]
        self.has_silver = row["Silver"]
        self.stripe_colour = row["Stripe Colour"]
