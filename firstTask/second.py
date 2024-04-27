number = float(input("Введите число:"))
sumPlus = 0.0
sumMinus = 0.0
startNumber = -number
finishNumber = number + 1
while startNumber < finishNumber:
    # print(startNumber)
    print(f"{startNumber:.1f}")
    if startNumber < 0:
        sumMinus += startNumber
    else: 
        sumPlus += startNumber
    startNumber += 0.1
    startNumber = round(startNumber, 1)
print("Сумма отрицательных чисел: "+str(sumMinus))
print("Сумма положительных чисел: "+str(sumPlus))