ships = "Б1В1Г1 Е4Е5 В4В5В6В7 Д3 Д6 З2К2"
ships_lower = ships.lower().replace(" ", "")
shot = input("Введите координаты выстрела (например, Б1): ").lower()
if shot in ships_lower:
    print("Попадание!")
else:
    print("Промах!")