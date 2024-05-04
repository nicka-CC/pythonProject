def zapisivatel(text: str, filename: str):
    with open(filename, 'a+',encoding='utf-8') as file:
        file.write(text + '\n')  
        file.seek(0)  
        lines = file.readlines()
    for index, line in enumerate(lines):
        if index % 2 == 1: 
            print(line.strip())  
zapisivatel("Пример текста для записи в файл", "./test.txt")
zapisivatel("Еще одна строка текста", "./test.txt")