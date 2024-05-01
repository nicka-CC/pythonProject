number = int(input("Какой размер множества вы хотите?"))
elements = []
for i in range(number):
    element = input(f" {i+1}: ")
    if element.isdigit():
        element = int(element)
        elements.append(element)
    else:
        elements.append(element)
    
def multiplyElements(elements: list, m: float = 2) -> list:
    return [element * m for element in elements]

mltplElmts = lambda elements, m=2: [element * m for element in elements]

print("Результат: ", multiplyElements(elements, 3))
print("Результат: ", mltplElmts(elements, 3))