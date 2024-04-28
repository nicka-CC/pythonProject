line = input("Введите строку, а я посчитаю количество символов в ней")
line = line.lower()
charCount={}
for i in line:
    if i != ' ' and i not in charCount:
        charCount[i] = line.count(i)

print(charCount)