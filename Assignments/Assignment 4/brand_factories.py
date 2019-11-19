import abc


class BrandFactory(abc.ABC):

    def create_shirt_men(self):
        pass

    def create_shirt_women(self):
        pass

    def create_socks_unisex(self):
        pass


class PineAppleRepublicFactory(BrandFactory):

    def create_shirt_men(self):
        return ShirtMenPineappleRepublic()

    def create_shirt_women(self):
        return ShirtWomenPineappleRepublic()

    def create_socks_unisex(self):
        return SockPairUnisexPineappleRepublic()


class NikaFactory(BrandFactory):

    def create_shirt_men(self):
        return ShirtMenNika()

    def create_shirt_women(self):
        return ShirtWomenNika()

    def create_socks_unisex(self):
        return SockPairUnisexNika()


class LuluLimeFactory(BrandFactory):

    def create_shirt_men(self):
        return ShirtMenLuluLime()

    def create_shirt_women(self):
        return ShirtWomenLuluLime()

    def create_socks_unisex(self):
        return SockPairUnisexLuluLime()


class ShirtMen(abc.ABC):

    def __init__(self, style, size, colour, textile):
        self.style = style
        self.size = size
        self.colour = colour
        self.textile = textile


class ShirtWomen(abc.ABC):

    def __init__(self, style, size, colour, textile):
        self.style = style
        self.size = size
        self.colour = colour
        self.textile = textile


class SockPairUnisex(abc.ABC):

    def __init__(self, style, size, colour, textile):
        self.style = style
        self.size = size
        self.colour = colour
        self.textile = textile


class ShirtMenLuluLime(ShirtMen):

    def __init__(self, style, size, colour, textile, category, hidden_zippers):
        self.style = style
        self.size = size
        self.colour = colour
        self.textile = textile
        self.category = category
        self.hidden_zippers = hidden_zippers


class ShirtMenPineappleRepublic(ShirtMen):

    def __init__(self, style, size, colour, textile, no_iron, buttons):
        self.style = style
        self.size = size
        self.colour = colour
        self.textile = textile
        self.no_iron = no_iron
        self.buttons = buttons


class ShirtMenNika(ShirtMen):

    def __init__(self, style, size, colour, textile, category):
        self.style = style
        self.size = size
        self.colour = colour
        self.textile = textile
        self.category = category


class ShirtWomenLuluLime(ShirtWomen):

    def __init__(self, style, size, colour, textile, category, hidden_zippers):
        self.style = style
        self.size = size
        self.colour = colour
        self.textile = textile
        self.category = category
        self.hidden_zippers = hidden_zippers


class ShirtWomenPineappleRepublic(ShirtWomen):

    def __init__(self, style, size, colour, textile, no_iron, buttons):
        self.style = style
        self.size = size
        self.colour = colour
        self.textile = textile
        self.no_iron = no_iron
        self.buttons = buttons


class ShirtWomenNika(ShirtWomen):

    def __init__(self, style, size, colour, textile, category):
        self.style = style
        self.size = size
        self.colour = colour
        self.textile = textile
        self.category = category


class SockPairUnisexLuluLime(SockPairUnisex):

    def __init__(self, style, size, colour, textile, has_silver, stripe_colour):
        self.style = style
        self.size = size
        self.colour = colour
        self.textile = textile
        self.has_silver = has_silver
        self.stripe_colour = stripe_colour


class SockPairUnisexPineappleRepublic(SockPairUnisex):

    def __init__(self, style, size, colour, textile, requires_dry_cleaning):
        self.style = style
        self.size = size
        self.colour = colour
        self.textile = textile
        self.requires_dry_cleaning = requires_dry_cleaning


class SockPairUnisexNika(SockPairUnisex):

    def __init__(self, style, size, colour, textile, is_articulated, sock_length):
        self.style = style
        self.size = size
        self.colour = colour
        self.textile = textile
        self.is_articulated = is_articulated
        self.sock_length = sock_length