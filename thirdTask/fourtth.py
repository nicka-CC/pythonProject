class Wallet:
    patSys: str = "MIR/UnionPay"
    def __init__(wall, name:str, currency: str):
        wall.balance= 0
        wall.name = name
        wall.currency = currency
        if currency not in ("BRB", "USD", "RUB"):
            raise ValueError(f"Это кошел поддерживает только эти валюты: BRB, EUR, RUB")
    def deposit(wall, plusBalance: float):
        if plusBalance < 0:
            raise ValueError(f"Вы не можете уйти в минус")
        wall.balance += plusBalance
        print(f"Ваш баланс был пополнен на {plusBalance}{wall.currency}. Текущий баланс равен {wall.balance}{wall.currency}")
    def pay(wall, minusBalance: float):
        if minusBalance < 0:
            raise ValueError(f"Вы не можете уйти в минус")
        if wall.balance >= minusBalance:
            wall.balance -= minusBalance
            print(f"Вы оплатили на {minusBalance}{wall.currency}. Текущий баланс равен {wall.balance}{wall.currency}")
        else:
            raise ValueError("У вас нахватает средств")
    def displayBalance(wall):
        print(f"Ваш баланс  {wall.balance}{wall.currency}")
    def deleteWallet(wall):
        wall.balance = 0
        print("Ваш кошеле очищен")
wallet = Wallet("My Wallet", "USD")
wallet.deposit(100)
wallet.pay(25)
wallet.displayBalance()
wallet.deleteWallet()