number = int(input("Какой размер множества вы хотите?"))
elements = []
for i in range(number):
    element = input(f" {i+1}: ")
    elements.append(element)
power = int(input("В какую степень множество нужно возвести?"))
result = []
for element in elements:
    if element.isdigit():
        element = int(element)
        number = element
        result.append(number ** power)
        
    else:
        result.append(element * power)
    
print(result)   