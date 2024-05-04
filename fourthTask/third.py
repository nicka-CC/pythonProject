def zapisivatel(text: str, filename: str):
    with open(filename, 'a+',encoding='utf-8')as file:
        file.write(text + '\n')  
        file.seek(0)  
        lines = file.readlines()
        if len(lines) % 2 == 0:
            print(text)
      
zapisivatel("Первый раз", "./fourthTask/test.txt")
zapisivatel("Второй раз", "./fourthTask/test.txt")
zapisivatel("Третий раз", "./fourthTask/test.txt")
zapisivatel("Четвертый раз", "./fourthTask/test.txt")
zapisivatel("Пятый раз", "./fourthTask/test.txt")