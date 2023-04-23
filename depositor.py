def depositor(how_money, input_valuta, input_id, purse):
    assert isinstance(input_id, object)
    if purse.get_id() == input_id:
        if purse.get_valuta()!=input_valuta:
            print("Невозможно зачислить деньги, осуществите перевод в нужную валюту")
            raise ValueError
        else:
            purse.money = purse.money + how_money
            purse.set_money(purse.money)


class Depositor:
    pass


