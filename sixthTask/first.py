def average_num(list_num: list) -> float:
    if not list_num:
        return "Bad request"
    for ind, el in enumerate(list_num):
        if not isinstance(el, (int, float)):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num) / len(list_num), 2)



assert average_num([1, 2, 3, 4, 5]) == 3.0, "Тест 1 не пройден"
assert average_num([1.0, 2.0, 3.0, 4.0, 5.0]) == 3.0, "Тест 2 не пройден"
assert average_num([1, 2, 3, 'a']) == "Bad request", "Тест 3 не пройден"
assert average_num(['1', '2', 3, 4]) == 2.5, "Тест 4 не пройден"
assert average_num([1.111, 2.299, 3.666]) == 2.36, "Тест 6 не пройден"
assert average_num([-1, -2, -3, -4, -5]) == -3.0, "Тест 7 не пройден"

assert isinstance(average_num([1, 2, 3]), float), "Тест 9 не пройден"
print("Все тесты пройдены успешно.")
