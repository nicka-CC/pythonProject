quadro: list[int] = [x ** 2 for x in range(1,11)]
daysWeek = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
Dictionary: dict[str, int] = {day: index + 1 for index, day in enumerate(daysWeek)}
libraries = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
libraryTeg: set[str] = {lib.lower() for lib in libraries}
print(quadro)
print(Dictionary)
print(libraryTeg)