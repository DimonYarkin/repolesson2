dictMonths = {1: ["Зима", 0], 2: ["Зима", 0], 3: ["Весна", 1], 4: ["Весна", 1], 5: ["Весна", 1], 6: ["Лето", 2],
              7: ["Лето", 2], 8: ["Лето", 2], 9: ["Осень", 3],
              10: ["Осень", 3], 11: ["Осень", 3], 12: ["Зима", 0]}
listMonths = ["Зима", "Весна", "Лето", "Осень"]
NumMonth = int(input("Введите номер месяца "))
if dictMonths.get(NumMonth) != None:
    print(f"Номер месяца соответствует времени года (из словоря): {dictMonths.get(NumMonth)[0]}")
    print(f"Номер месяца соответствует времени года (из списка): {listMonths[dictMonths.get(NumMonth)[1]]}")
else:
    print("По номеру месца время года не найдено!!!")
