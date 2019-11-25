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
            apple = row_["Garment"]
            orange = row_["Dry Cleaning"]
            print(apple)
            print(orange)
        if row_.Brand == "PineappleRepublic":
            print(row_["Brand"])
        if row_.Brand == "Nika":
            print(row_["Brand"])


def main():
    op = OrderProcessor('COMP_3522_A4_orders.xlsx')
    ef = op.read_order()
    op.process_order(0)


if __name__ == '__main__':
    main()