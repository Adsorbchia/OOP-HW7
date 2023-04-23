from typing import List, Any

import find
from depositor import depositor

from purse import Purse
from withdraw_money import withdraw_money
from x import X, x
from y import Y, y


# банковское приложение

class Main:
    x.info()  # выводим на экран баланс пользователя
    print("_________________________")
    print("Зачисляем")
    depositor(100, "USA", 1, x)  # Зачислить 100 на баланс пользователя (id=1)

    print(x.get_name())
    print(x.get_money())
    print("Снимаем")

    withdraw_money(200, 1, x)  # Снять со счета пользователя(id=1) 220
    print(x.get_money())
