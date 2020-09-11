goods = []
features = {'Наименование': '', 'Цена': '', 'Колическво': '', 'Ед': ''}
analytics = {'Наименование': [], 'Цена': [], 'Колическво': [], 'Ед': []}
num = 0
feature_ = None
control = None
while True:
    control = input("Для выхода введите 'Q', нажмите 'Enter', для ввода товара 'A'").upper()
    if control == 'Q':
        break
    num += 1
    if control == 'A':

        for f in features.keys():
            feature_ = input(f'Введите значение: "{f}"')
            features[f] = int(feature_) if (f == 'Цена' or f == 'Колическво') else feature_

    goods.append((num, features))
print(f'\n Список введнных товаров \n {"-" * 30}')
for i in range(int(len(goods))):
    print(f'{"Товар №" :>30}: {goods[i][0]}')
    for key, value in goods[i][1].items():
        print(f'{key[:25]:>30}: {value}')
        print("-" * 30)
