number = input("Введите трехзначное число: ")

if len(number) != 3 or not number.isdigit() or len(set(number)) != 3:
    print("Необходимо ввести трехзначное число с уникальными цифрами!!!!")
else:
    print("Возможные перестановки цифр:")

    used = set()
    for p in range(3):
        for s in range(3):
            if s != p:
                for t in range(3):
                    if t != p and t != s:
                        permutation = number[p] + number[s] + number[t]
                        if permutation not in used:  
                            used.add(permutation)
                            print(permutation)