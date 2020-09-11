userStr = input("Введите строку ")
listWord = userStr.split()
i = 0
for i in range(len(listWord)):
    if len(listWord[i]) > 10:
        print(f"номер по порядку {i + 1} слово {listWord[i][0:10]}")
    else:
        print(f"номер по порядку {i + 1} слово {listWord[i]}")
