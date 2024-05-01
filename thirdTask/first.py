def plus(x,y):
    return x + y
def minus(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    if y == 0:
        raise ValueError("Вы не можете делить на ноль")
    return x / y
def stepen(x,y):
    return x ** y
def checkNumber(value):
    numberInput = input(value)

    numberInput = float(numberInput)
    if not isinstance(numberInput, (int, float)):
        raise ValueError("Это не число")
    return numberInput

        
       
def calculator():
    while True:
        print("Выберите действие:")
        print("'+' Сложение")
        print("'-' Вычитание")
        print("'*' Умножение")
        print("'/' Деление")
        print("'^' Возведение в степень")
        print("'ESC' Выход")
        choise = input("Выберите действие (пропишите его без кавычек)")
        if choise == 'ESC':
            print("Мы закончили")
            break
        if choise not in ('+', '-', '*', '/', '^', 'ESC'):
            print("Такого действия нет! Повторите попытку!")
            continue
        numFirst = checkNumber("Первое число:")
        numSec = checkNumber("Второе число:")
        try:
            if choise == '+':
                print("Результат: ", plus(numFirst, numSec))
            elif choise == '-':
                print("Результат: ", minus(numFirst, numSec))
            elif choise == '*':
                print("Результат: ", multiply(numFirst, numSec))
            elif choise == '/':
                print("Результат: ", divide(numFirst, numSec))
            elif choise == '^':
                print("Результат: ", stepen(numFirst, numSec))

        except ValueError as e:
            print(e)

if __name__ == "__main__":
    calculator()