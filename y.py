from purse import Purse


class Y(Purse):
    __id = 2

    def get_id(self):
        return self.__id

    def __init__(self, name, money, valuta):
        super().__init__(name, money, valuta)
        self.__id = 2

    @staticmethod
    def info():
        print(y.get_name())
        print(y.get_money())


y = Y("Игорь_Гончаров", 100, "USA")

y.set_name("Игорь Гончаров")
y.set_money(100)
y.set_valuta("USA")

