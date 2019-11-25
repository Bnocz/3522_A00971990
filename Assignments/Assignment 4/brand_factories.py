import abc


class BrandFactory(abc.ABC):
    """
    Abstract class for all BrandFactories. Has empty methods
    to create ShirtMen, ShirtWomen, and SockPairUnisex
    """
    def __init__(self, order):
        self.order = order

    def create_shirt_men(self):
        pass

    def create_shirt_women(self):
        pass

    def create_socks_unisex(self):
        pass


class PineAppleRepublicFactory(BrandFactory):
    """
    Brand factory for PineappleRepublic. The other BrandFactories
    are identical except for the return type being their own
    brand of clothing.
    """

    def create_shirt_men(self):
        return ShirtMenPineappleRepublic(self.order.style, self.order.size, self.order.colour,
                                         self.order.textile, self.order.no_iron, self.order.buttons)

    def create_shirt_women(self):
        return ShirtWomenPineappleRepublic(self.order.style, self.order.size, self.order.colour,
                                           self.order.textile, self.order.no_iron, self.order.buttons)

    def create_socks_unisex(self):
        return SockPairUnisexPineappleRepublic(self.order.style, self.order.size, self.order.colour,
                                               self.order.textile, self.order.requires_dry_cleaning)


class NikaFactory(BrandFactory):

    def create_shirt_men(self):
        return ShirtMenNika(self.order.style, self.order.size, self.order.colour,
                            self.order.textile, self.order.category)

    def create_shirt_women(self):
        return ShirtWomenNika(self.order.style, self.order.size, self.order.colour,
                              self.order.textile, self.order.category)

    def create_socks_unisex(self):
        return SockPairUnisexNika(self.order.style, self.order.size, self.order.colour,
                                  self.order.textile, self.order.is_articulated,
                                  self.order.sock_length)


class LuluLimeFactory(BrandFactory):

    def create_shirt_men(self):
        return ShirtMenLuluLime(self.order.style, self.order.size, self.order.colour,
                                self.order.textile, self.order.category, self.order.hidden_zippers)

    def create_shirt_women(self):
        return ShirtWomenLuluLime(self.order.style, self.order.size, self.order.colour,
                                  self.order.textile, self.order.category, self.order.hidden_zippers)

    def create_socks_unisex(self):
        return SockPairUnisexLuluLime(self.order.style, self.order.size, self.order.colour,
                                      self.order.textile, self.order.has_silver, self.order.stripe_colour)


class ShirtMen(abc.ABC):
    """
    Abstract class for a ShirtMen, has variables applicable to all
    shirts
    """

    def __init__(self, style, size, colour, textile):
        self.style = style
        self.size = size
        self.colour = colour
        self.textile = textile


class ShirtWomen(abc.ABC):
    """
    Abstract class for a ShirtWomen, has variables applicable to all
    shirts
    """

    def __init__(self, style, size, colour, textile):
        self.style = style
        self.size = size
        self.colour = colour
        self.textile = textile


class SockPairUnisex(abc.ABC):
    """
    Abstract class for a SockPairUnisex, has variables applicable to all
    socks
    """

    def __init__(self, style, size, colour, textile):
        self.style = style
        self.size = size
        self.colour = colour
        self.textile = textile


class ShirtMenLuluLime(ShirtMen):
    """
    Brand specific ShirtMen object. Has variables category, and hidden_zippers
    which are specific to luluLime
    """

    def __init__(self, style, size, colour, textile, category, hidden_zippers):
        super().__init__(style, size, colour, textile)
        self.category = category
        self.hidden_zippers = hidden_zippers


class ShirtMenPineappleRepublic(ShirtMen):
    """
    PineappleRepublic brand ShirtMen, have variables for whether you can
    iron or if it has extra buttons
    """

    def __init__(self, style, size, colour, textile, no_iron, buttons):
        super().__init__(style, size, colour, textile)
        self.no_iron = no_iron
        self.buttons = buttons


class ShirtMenNika(ShirtMen):
    """
    Nika brand ShirtMen, have variables for whether it is sports or outdoor clothing
    """

    def __init__(self, style, size, colour, textile, category):
        super().__init__(style, size, colour, textile)
        self.category = category


class ShirtWomenLuluLime(ShirtWomen):
    """
    Brand specific ShirtWomen object. Has variables category, and hidden_zippers
    which are specific to luluLime
    """
    def __init__(self, style, size, colour, textile, category, hidden_zippers):
        super().__init__(style, size, colour, textile)
        self.category = category
        self.hidden_zippers = hidden_zippers


class ShirtWomenPineappleRepublic(ShirtWomen):
    """
    PineappleRepublic brand ShirtWomen, have variables for whether you can
    iron or if it has extra buttons
    """
    def __init__(self, style, size, colour, textile, no_iron, buttons):
        super().__init__(style, size, colour, textile)
        self.no_iron = no_iron
        self.buttons = buttons


class ShirtWomenNika(ShirtWomen):
    """
    Nika brand ShirtWomen, have variables for whether it is sports or outdoor clothing
    """
    def __init__(self, style, size, colour, textile, category):
        super().__init__(style, size, colour, textile)
        self.category = category


class SockPairUnisexLuluLime(SockPairUnisex):

    def __init__(self, style, size, colour, textile, has_silver, stripe_colour):
        super().__init__(style, size, colour, textile)
        self.has_silver = has_silver
        self.stripe_colour = stripe_colour


class SockPairUnisexPineappleRepublic(SockPairUnisex):

    def __init__(self, style, size, colour, textile, requires_dry_cleaning):
        super().__init__(style, size, colour, textile)
        self.requires_dry_cleaning = requires_dry_cleaning


class SockPairUnisexNika(SockPairUnisex):

    def __init__(self, style, size, colour, textile, is_articulated, sock_length):
        super().__init__(style, size, colour, textile)
        self.is_articulated = is_articulated
        self.sock_length = sock_length
