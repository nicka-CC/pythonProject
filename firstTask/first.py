while True:
    number = input("Вводи числа (одно число в строчку), а я посчитаю тебе длину. Для выхода пропиши 'exit' без кавычек: ")  

    if number.lower() == "exit":  
        print("Вы вышли.")
        break

    float(number)
    if number.type() == float:
        isNumber = True  
    else: isNumber = False

    if isNumber:
        if '.' in number or '-' in number:
            numberLength = len(number.replace("-", "").replace(".", ""))
        else:
            numberLength = len(number)
        print("Длина введенного числа:", numberLength)
    else:
        print('Эй! Я же сказал, введи число!!!')
