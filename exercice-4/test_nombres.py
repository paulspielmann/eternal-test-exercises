import art


def number2anybase(num: int, base: int):
    """Prends en argument un nombre entier a convertir et une base, retourne un iterateur sur la liste de bit/digit associe"""
    digits = []
    while num:
        digits.append(num % base)
        num //= base
    return reversed(digits)


class NumberDisplay:
    """Creer un objet number display avec comme attribut un entier ainsi qu'une base source (10 par defaut)"""
    TYPE_NUMBERS = {
        "16": "0123456789ABCDEF",
        "10": "0123456789",
        "secret": "OIZELVG#Bq",
    }

    def __init__(self, display_len: int = 4, code: str = "10"):
        self.display_len = display_len
        self.encoding = code

    """Retrieve la base desiree et la base actuelle, encode le nombre actuelle dans la base desiree avec number2anybase()
    et print to stdout l'ascii art associe"""
    def show_number(self, number: str, number_source_base: int):
        our_encoding = self.TYPE_NUMBERS[self.encoding]
        our_base = len(our_encoding)
        to_show = "".join(
            our_encoding[a]
            for a in number2anybase(int(number, base=number_source_base), our_base)
        ).rjust(self.display_len, our_encoding[0])
        art.tprint(to_show)

nd = NumberDisplay(display_len = 4, code = "10")

nd.show_number("AB", 16)
