from purse import Purse


class X(Purse):
    __id = 1

    def __init__(self, name, money, valuta):
        super().__init__(name, money, valuta)
        self.__id = 1

    def get_id(self):
        return self.__id

    @staticmethod
    def info():
        print(x.get_name())
        print(x.get_money())



x = X("name", 0.00, "USA")

x.set_name("Ирина_Петрова")
x.set_money(110)
x.set_valuta("USA")


