name = input("Введите ваше имя: ")
surname = input("Введите вашу фамилию: ")
age = input("Введите ваш возраст: ")
infoFormat = "Ваше имя: {0}, Фамилия: {1}, Возраст: {2} лет.".format(name, surname, age)
infoFString = f"Ваше имя: {name}, Фамилия: {surname}, Возраст: {age} лет."
print("Пример формата: "+infoFormat)
print("Пример ЭФ-тринга: "+infoFString)