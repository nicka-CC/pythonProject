count = int(input("Введите числом количество желаемых чисел"))
def fibonachi(number: int):
    a: int = 1
    b: int =  1
    count: int = 0
    while count < number:
        yield a
        a, b = b, a + b
        count += 1
for number in fibonachi(count):
    print(number)