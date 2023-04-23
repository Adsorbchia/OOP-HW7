def withdraw_money(how_money, input_id, purse):
    assert isinstance(input_id, object)
    if purse.get_id() == input_id:
        if purse.get_money() < how_money:
            print("не достаточно средств")
            raise ValueError
        else:
            purse.money = purse.money - how_money
            purse.set_money(purse.money)


class Withdraw_money:
    pass
