my_list = [7, 5, 3, 3, 2]
userValue = int(input("Введите число (для выхода введите 111): "))
while userValue != 111:
    if userValue > my_list[0]:
        my_list.insert(0, userValue)
    else:
        for i, e in reversed(list(enumerate(my_list))):
            if userValue == e or userValue < e:
                my_list.insert(i + 1, userValue)
                break
    print(my_list)
    userValue = int(input("Введите число (для выхода введите 111): "))
print("Работа с программой завершена!!!")