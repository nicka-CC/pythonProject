def decorator(func):
    def wrapper(*args:any, **kwargs:any):
        argsW = [repr(a) for a in args]
        kwargsW = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(argsW + kwargsW)
        print(f"Вызывается функция {func.__name__} с аргументами ({signature})")
        yield from func(*args, **kwargs)
    return wrapper

@decorator
def fibonacci(number: int):
    a, b = 1, 1
    count = 0
    while count < number:
        yield a
        a, b = b, a + b
        count += 1

count = int(input("Введите числом количество желаемых чисел: "))
for number in fibonacci(count):
    print(number)
