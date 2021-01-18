#=====#1=====

x = [100, False, 0.5, 'Привет мир', b'\x00\x00\x00', 1j+3, {1: 5}, int, None, ]
for x in x:
    print(type(x))

#=====#2=====

import random

z = random.randint(3, 9)
print(f"Введите элементы в количестве {z-1} штук:")

#Формируем список:
x = []
for i in range(1,z):
    x.append(input("Ввод: ", ))
print(f"Спасибо, исходный список выглядет так:{x}")

#Меняем местами элементы:
y = int(len(x))
print(f"Всего элементов в списке: {y}, каждая итерация меняет местами минимум два элемента, "
      f"значит элементы, делим на два и получаем количество итераций равное: {y // 2}")

n = 0 #Номер элемента
for i in range(int(y//2)):
    x[n], x[n + 1] = x[n + 1], x[n]
    n += 2 #потому что на первой итерации 0-1, на второй 2-3, на третьей 4-5 и т.д.
print(x)

#=====#3=====

time_years_1 =  ['зима', 'весна', 'лето', 'осень']
time_years_2 = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето',
                8: 'лето', 9: 'осень', 10: 'осень', 11: 'осень', 12: 'зима'}

print("Введите номер месяца: ")
x = int(input())

#В словаре:
for x in range(x+1):
        pass
if x > 12:
        print ("На нашей планете, нет такого месяца, быть может Вы с другой?")
else:
        print("В словаре это:", time_years_2.get(x))

#В списке:
if x == 1 or x == 2 or x == 12:
        print ("В списке это:", time_years_1[0])
elif x == 3 or x == 4 or x == 5:
        print("В списке это:", time_years_1[1])
elif x == 6 or x == 7 or x == 8:
        print("В списке это:", time_years_1[2])
elif x == 9 or x == 10 or x == 11:
        print("В списке это:", time_years_1[3])
else:
        pass

#=====#4=====

x = input("Напишите Ваше предложение: ")
y = list(x.split(" "))
i = 0

for y in y:
        i += 1
        print(f"{i}.", y[0:10])

#=====#5=====

my_list = [7, 5, 3, 3, 2]

x = int(input(f"Добавьте новый элемент к следующему: {my_list} рейтингу: "))

y = my_list.count(x)  # Выясняем длинну в конце которой необходимо добавить э-т.

for i in range(len(my_list)):
    if x < my_list[int(len(my_list)-1)]:
        my_list.insert(int(len(my_list)), x)  # В конец.
    elif x > my_list[0]:
        my_list.insert(0, x)  # В начало.
    elif x < my_list[i-1] and x > my_list[i]:
        my_list.insert(i, x)  # Между.
        break
    elif x == my_list[i]:
        my_list.insert(i + y, x)  # Добавляем в конец найденного y.
        break

print(f" Новый рейтинг теперь выглядит так: {my_list}")

#=====#6=====

total = int(input("Введите общее число товаров: ", ))

n = 1
x = []
x1 = []
z = {"название": '', "цена": '', "количество": '', "eд": ''}
z1 = {"название": [], "цена": [], "количество": [], "eд": []}

var = int(input("Выберите вариант <1> - чтобы  получить список, или <2> - анализ: ", ))

if var == 1:
    for i in range(total):
        x = dict({"название": input("введите название: "), "цена": input("введите цену: "),
                    "количество": input("введите количество: "), "eд": input("введите единицу измерения: ")})
        x1.append((n, x))
        n += 1

    print(x1)

if var == 2:
    for i in range(total):
        for i in z.keys():
            z[i] = input(f'введите "{i}"')
            z1[i].append(z[i])

    print(z1)