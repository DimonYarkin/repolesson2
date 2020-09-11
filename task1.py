myNewList = [12, None, -77, 'True', True, 9.5, [1, 2], (3, 2), {1: 'one'}]


def myNewType(el):
    for el in range(len(myNewList)):
        print(type(myNewList[el]))
    return


myNewType(myNewList)
