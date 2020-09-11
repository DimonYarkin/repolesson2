countElement = int(input("Введите количество элементов списка "))
myNewList = []
i = 0
el = 0
while i < countElement:
    myNewList.append(input("Введите следующее значение списка "))
    i += 1

for elem in range(int(len(myNewList) / 2)):
    myNewList[el], myNewList[el + 1] = myNewList[el + 1], myNewList[el]
    el += 2
print(myNewList)
