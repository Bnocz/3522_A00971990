import pandas
import brand_factories


class OrderProcessor:

    def __init__(self, file_path):
        self.file_path = "COMP_3522_A4_orders.xlsx"
        self.order = None

    def read_order(self):
        self.order = pandas.read_excel(self.file_path)
        return self.order

    def process_order(self, index_):
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

    def __init__(self, row, factory):
        self.row = row
        self.factory = factory
        self.garment = row["Garment"]
        self.count = row["Count"]
        self.style_name = row["Style Name"]
        self.size = row["Size"]
        self.Colour = row["Colour"]
        self.textile = row["Textile"]



def main():
    op = OrderProcessor('COMP_3522_A4_orders.xlsx')
    ef = op.read_order()
    op.process_order(0)


if __name__ == '__main__':
    main()