class Purse:

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_money(self):
        return self.money

    def set_money(self, money):
        self.money = money

    def get_valuta(self):
        return self.valuta

    def set_valuta(self, valuta):
        self.valuta = valuta

    def __init__(self, __name, __money, __valuta):
        self.name = __name
        self.money = __money
        self.valuta = __valuta
