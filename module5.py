# def get_wind_class(speed):  # Объявление функции
#     if speed >= 1 and speed <= 4:
#         return ('weak [1]')
#     elif speed > 4 and speed <= 10:
#         return ('moderate [2]')
#     elif speed > 10 and speed <= 18:
#         return ('strong [3]')
#     elif speed > 18:
#         return ('hurricane [4]')
#
#
#
# print(get_wind_class(1))

'''
Допишите функцию check_user так, чтобы она по логину пользователя
проверяла, существует он или нет,
после чего с помощью вложенного условия проверяла
правильность пароля этого пользователя.
Функция должна возвращать только True или False.
Чтобы вернуть True, напишите "return True";
чтобы вернуть False, напишите "return False".
'''
# user_database = {
#     'user': 'password',
#     'iseedeadpeople': 'greedisgood',
#     'hesoyam': 'tgm'
# }
# def check_user(username, password):
#     if username in user_database:
#         if user_database[username] == password:
#             return True
#         else:
#             return False
#     else:
#         return False

# num = 12344321
#
# print(str(num) == str(num)[::-1])
# import time
import time

'''ЗАДАНИЕ 1.2 (НА САМОПРОВЕРКУ)
Условие задачи. Найти сумму всех натуральных чисел от 1 до N включительно.'''

# n = input('Enter number: ')
# n = range(1, int(n) + 1)
# print(n)
# sum = 0
# for i in n:
#     sum = sum + i
#     print (f'{sum-i}+{i}={sum}')
'''
ЗАДАНИЕ 1.3 (НА САМОПРОВЕРКУ)
Напишите программу, которая будет печатать лесенку следующего типа:

n = 3
*
**
***

n = 4
*
**
***
****
Число n может быть любым.'''

# import time
#
# n = input('Enter number: ')
# n = range(1, int(n) + 1)
# print(n)
# for i in n:
#     print(f'{i} - {"*" * i}')
#     time.sleep(0.6)

# my_list = [1]
# for i in range(10):
#     my_list.append(my_list[i] * 2)
#     print(my_list)
# my_list.sort(reverse = True)
# print(my_list)
# print(my_list[6])
'''Задание 1.7

Создайте список word_list = ['My', 'name', 'is', 'ваше имя на латинице (например, Sergei)']. Напишите цикл, 
который складывает все строки из списка в одно предложение, и выведите это предложение на экран. Запишите в ответ 
получившееся предложение. '''

# word_list = ['My', 'name', 'is', 'Sergei']
# str1 = ""
# for i in range(len(word_list)):
#     str1 = str(str1) + str(word_list[i] + " ")
#     print(word_list[i])
# print (str1)


'''Задание 1.8
1 point possible (graded)
Создайте список num_list = [1, 10, 3, -5].
Отсортируйте его с помощью метода sort() для списков.
Последовательно выведите на экран элементы этого списка с помощью цикла for.
В ответ запишите последний выведенный на экран элемент.'''

# num_list = [1, 10, 3, -5]
# print (num_list)
# num_list.sort()
# print (num_list)
# for i in range(len(num_list)):
#     print (num_list[i])

'''Задание 1.9 Создайте список my_list = list(range(0, 100, 3)). С помощью цикла for 
посчитайте количество элементов в списке. В ответ запишите получившееся число. '''

# my_list = list(range(0, 100, 3))
# # print (len(my_list))
# counter = 0
# for i in my_list:
#     counter += 1
#     print ((counter), " ", (i))

'''Задание 1.10  Создайте список my_list = [True, 1, -10, 'hello', False, 'string_1', 123, 
2.5, [1, 2], 'another']. С помощью цикла for посчитайте количество элементов типа str в списке. В ответ запишите 
получившееся число. '''

# my_list = [True, 1, -10, 'hello', False, 'string_1', 123,
#            2.5, [1, 2], 'another']
# count = 0
# for i in my_list:
#     print (type(i), end = "\t\t"); print(i)
#     if type(i) == str:
#         count = count+1
#     time.sleep(0.3)
#
#
# print (f'''\nКоличество элементов типа "СТРОКА" - {count}''')

'''Условие задачи. Написать цикл, который будет складывать натуральные числа, пока их сумма не превысит 500'''

# sum = 0
# n = 1
# while sum < 500:
#     print(n, end = "\t - \t"); print (f'{sum} + {n} = {sum+n}')
#     sum += n
#     n +=1
# print (sum)

'''ЗАДАНИЕ 2.1 (НА САМОПРОВЕРКУ)

Напишите цикл while, который находит максимальное натуральное число, квадрат которого меньше 1000.'''

# x = 0
# n = 1
# while x < 1000:
#     x = n ** 2
#     n += 1
# print (n-1)
# print (x)

'''Задание 2.9
Напишите программу, которая считает неотрицательные степени двойки до тех 
пор, пока это число не станет больше 10 000. В ответ запишите количество итераций, которые проделывает цикл. '''

# n = 1
# count = 0
# x = 0
# while x < 10000:
#     count += 1
#     x = 2 ** n
#     print (f'Итерация {count} - 2^{n}={x}')
#     n += 1
#
# print(f'Количество итераций цикла равно - {count}')

'''ЗАДАНИЕ 2.10 (НА САМОПРОВЕРКУ)

Сгенерируйте случайное число в диапазоне от 0 до 10 000 с помощью модуля random следующим образом:

import random
num = random.randint(0, 10000)
С помощью цикла while и математических операций определите наименьшую цифру в этом числе.'''

# import random
#
# num = random.randint(0, 1000000)
# print(f'Сгенерированное число - {num}')
# x=num
# str = []
# while x != 0:
#     str.append(x%10)
#     x = x // 10
#
# str.sort()
# print (f'Минимальная цифра в числе {num} это {str[0]}')


'''Задание 2.11 
Олег положил тысячу рублей в банк под 8% годовых. Через сколько лет у него 
на счету будет не менее трёх тысяч рублей? Выведите на экран это число и запишите его в ответ. '''
# vklad = 1000
# count = 0
# while vklad < 3000:
#     vklad = vklad * 1.08
#     count += 1
#     print (vklad)
#     print (count)
# print (count-1)

'''Задание 2.12 


От коллеги вам достался код, который почему-то зацикливается и не даёт никакого результата. Ваша задача — исправить 
этот код. Запишите в ответ строку, которую вы добавили. '''
#
# employee = 5
# i = 1
# while i < employee:
#     if i > 1:
#         print('There are', i, 'people in the department') # В отделе i человек
#     if i == 1:
#         print('There are', i, 'people in the department') # В отделе i человек
#     i += 1

'''Условие задачи. Дана двумерная матрица 3x3 (двумерный массив). Определить максимум и минимум каждой строки, 
а также их индексы. '''
#
# random_matrix = [
#     [9, 2, 1],
#     [2, 5, 3],
#     [4, 8, 5]
# ]
#
# # print (min(random_matrix[0]))
#
# list_ = [-5, 2, 4, 8, 12, -7, 5]
# # Функция enumerate возвращает данные в виде кортежей,
# # где на первом месте стоит индекс, а затем значение
# # [(0, -5), (1, 2), (2, 4), ...]
# a = enumerate(list_)
# print(list(a))
# print (a)
# b=list(a)
# print (b)
# # for i, value in enumerate(list_):
# #     print("Element index: ", i) # индекс элемента
# #     print("Element value: ", value)  # с помощью индекса получаем значение элемента
# #     print("---")
# # print("End of the cycle") # конец цикла


# text = """ The rabbit-hole went straight on like a tunnel for some way, and then dipped suddenly down, so suddenly
# that Alice had not a moment to think about stopping herself before she found herself falling down a very deep well.
#
# Either the well was very deep, or she fell very slowly, for she had plenty of time as she went down to look about
# her and to wonder what was going to happen next. First, she tried to look down and make out what she was coming to,
# but it was too dark to see anything; then she looked at the sides of the well, and noticed that they were filled
# with cupboards and book-shelves; here and there she saw maps and pictures hung upon pegs. She took down a jar from
# one of the shelves as she passed; it was labelled `ORANGE MARMALADE', but to her great disappointment it was empty:
# she did not like to drop the jar for fear of killing somebody, so managed to put it into one of the cupboards as
# she fell past it.
#
# `Well!' thought Alice to herself, `after such a fall as this, I shall think nothing of tumbling down stairs! How
# brave they'll all think me at home! Why, I wouldn't say anything about it, even if I fell off the top of the
# house!' (Which was very likely true.) """

# text = text.lower()
# text = text.replace(" ", "")
# text = text.replace("\n", "")
# print(text)
# count = {}  # для подсчёта символов и их количества
# for char in text:
#     if char in count:  # если символ уже встречался, увеличиваем его количество на 1
#         count[char] += 1
#     else:
#         count[char] = 1
# print(count)
# for char, cnt in count.items():
#     print(f"Symbol {char} can be found {cnt} times in the text")

'''ЗАДАНИЕ 4.2 (НА САМОПРОВЕРКУ)

Дана строка:

letters_string = 'kjdKJKSJLKJFLkalsdLAJdjlaksIdakLJDLAs'
Ваша задача — привести все символы строки к нижнему регистру.

Помните, что строки — неизменяемый тип данных.'''

# letters_string = '''kjdKJKSJLKJFLkalsdLAJdjlaksIdakLJDLAs'''
# letter=letters_string.lower()
# print(letter)
# count = {}
# for char in letter:
#     if char in count:
#         count[char] += 1
#     else:
#         count[char] = 1
# print (count)
# for char in count:
#     print(f'Символ {char} встречается {count[char]} раз')


'''# Допишите функцию check_h так, чтобы она проверяла гипотезу Сиракуз для числа n.

# Гипотеза Сиракуз заключается в том,
# что любое натуральное число можно свести к 1,
# если повторять над ним следующие действия:
# если число четное, то разделить его пополам,
# если нечетное - умножить на 3, прибавить 1 и результат разделить на 2.'''

# def check_h(n):
#     while n > 1:
#         if n % 2 == 0 and n != 1:
#             n = n / 2
#         if n % 2 == 1 and n != 1:
#             n = (n*3+1)/2
#         if n == 1:
#             return True
#
#     return False
#
# print (check_h(2))

# heads = 71  # количество голов
# legs = 178  # количество ног
#
# for r in range(heads + 1):  # количество кроликов
#     for ph in range(heads + 1):  # количество фазанов
#         #  если суммарное количество голов или ног превышено, переходим на следующий шаг цикла
#         if (r + ph) > heads or \
#             (r * 4 + ph * 2) > legs:
#             continue
#         if (r + ph) == heads and (r * 4 + ph * 2) == legs:
#             print("Number of rabbits", r) # количество кроликов
#             print("Number of pheasants", ph) # количество фазанов
#             print("---")


'''ЗАДАНИЕ 5.1 (НА САМОПРОВЕРКУ)

Создайте список из 10 рандомных чисел с помощью модуля random следующим образом:

import random
my_list = []
for i in range(0, 10):
    my_list.append(random.randint(0, 10))
Необходимо вывести на экран yes, если в списке есть одинаковые числа, и no, если одинаковые числа отсутствуют.

'''

# import random
#
# my_list = []
# for i in range(0, 10):
#     my_list.append(random.randint(0, 99))
# print(my_list)
# yes = 0
# no = 0
# for m in range(len(my_list)):
#     # print(m)
#     if my_list.count(my_list[m]) > 1:
#         yes += 1
#         # print ("Yes")
#         # break
#     else:
#         no += 1
#         # print ("No")
# if yes > 0:
#     print ("Yes")
# else:
#     print("No")
#
# # print(my_list[0])
# # print(my_list.count(my_list[0]))


'''ЗАДАНИЕ 5.2 (НА САМОПРОВЕРКУ)

Задайте некоторый список my_list, содержащий целые числа, с помощью модуля random, как и в предыдущей задаче.

Используя инструкцию while, разработайте программу, которая вычисляет сумму элементов списка.'''

# import random, time
#
# my_list = []
# for i in range(10):
#     my_list.append(random.randint(0, 9999))
# print(my_list)
# m = 0
# sum = 0
# while m in range(len(my_list)):
#     sum = sum + my_list[m]
#     print (f'Число {m+1} = {my_list[m]},\t нарастающий итог - {sum}')
#     m += 1
#     time.sleep(0.5)
# print (f'Итоговая сумма списка {my_list} равна {sum}')

'''Задание 5.3

Задан список из строк:
str_list = ['text', 'morning', 'notepad', 'television', 'ornament']
Подсчитайте количество вхождений символа 't' в каждую из строк этого списка.

Используйте словарь: в качестве ключа запишите в него строку, в качестве значения — число вхождений буквы 't' в эту 
строку (пример вывода: {'letter': 2, 'hello': 0}). 

В качестве ответа введите результат вывода.'''

# str_list = ['text', 'morning', 'notepad', 'television', 'ornament']
# m=0
# itog = {}
# while m in range(len(str_list)):
#     print (str_list[m].count('t'))
#     itog[str_list[m]] = str_list[m].count('t')
#     m+=1
# print(itog)

'''Задание 5.4 1 point possible (graded) Вы играете в компьютерную игру, дошли до схватки с финальным боссом, 
но вот незадача: ваш компьютер «заглючил», и вы не можете управлять вашим персонажем. Босс атакует и каждую секунду 
наносит один удар, который отнимает у персонажа 80 единиц здоровья. На схватку с боссом ваш персонаж вышел с 500 
единицами здоровья. 

Создайте цикл, позволяющий понять, через сколько секунд босс убьёт вашего персонажа.

Для проверки используйте переменную current_health для сохранения текущего уровня здоровья и изменяйте её по ходу 
цикла, а также переменную attack = 80 для хранения значения атаки Босса. 

В результате работы программа должна вывести на экран количество секунд, в течение которых будет длиться схватка. 
Ответ должен быть выведен на экран в виде целого числа без какого-либо дополнительного поясняющего текста. '''

# current_health = 500
# attack = 80
# count = 0
# while current_health > 0:
#     current_health = current_health - attack
#     count += 1
# print (count)

'''ЗАДАНИЕ 5.5 (НА САМОПРОВЕРКУ)

С помощью модуля random создайте список с тремя случайными числами в диапазоне от 0 до 100 000:

import random
my_list = []
for i in range(3):
    my_list.append(random.randint(0, 100000))
Среди этих чисел найдите наибольшее по сумме цифр и выведите его на экран.

В этой задаче можно использовать комбинацию циклов for и while.'''

# import random
# my_list = []
# for i in range(3):
#     my_list.append(random.randint(0, 100000))
#
# print(f'Система создала список:\n{my_list}\n')
# list = []
# for m in range(len(my_list)):
#         number = my_list[m]
#         sum = 0
#         while number != 0:
#             sum = sum + number % 10
#             number = number // 10
#         print(f'Сумма цифр числа {my_list[m]}\tравна {sum}')
#         list.append(sum)
# list.sort()
# print (f'\nМаксимальная сумма цифр - {list[-1]}')
#
# sentence = "A roboT MAY Not injure a humAn BEING or tHROugh INACtion allow a human BEING to come to harm"
# sentence = sentence.lower()
# word_list = sentence.split()
# word_list.sort()
# word_dict = {}
# for word in word_list:
#     if word not in word_dict.keys():
#         word_dict[word] = word_list.count(word)
#
# print(word_dict)


import phonenumbers

# from phonenumbers import timezone

# my_number = phonenumbers.parse("+7(39197)2-42-29")
# print(timezone.time_zones_for_number(my_number))

'''ЗАДАНИЕ 2.3 (ВЫПОЛНЯЕТСЯ В CODEBOARD НИЖЕ)

?

Напишите функцию get_total, которая принимает на вход число единиц товара и стоимость каждой единицы. Функция 
возвращает одно число — общую стоимость данного числа товаров. 

Пример:

print(get_total(15, 50))
# 750'''

# def get_total (quantity, price):
#
#     return quantity * price
# print(get_total(15, 50))


'''ЗАДАНИЕ 3.1 (ВЫПОЛНЯЕТСЯ В CODEBOARD НИЖЕ)

?

Попробуйте добавить в новую функцию get_time из примера выше проверку скорости на равенство нулю. Если скорость равна 
нулю, верните ValueError с сообщением "Speed cannot be equal to 0!". 

Вы можете проверить своё решение, вызвав функцию get_time:'''

# def get_time(distance, speed):
#     if distance < 0 or speed < 0:
#         raise ValueError("Distance or speed cannot be below 0!")
#     if speed == 0:
#         raise ValueError('Speed cannot be equal to 0!')
#     return distance / speed
#
#
# print(get_time(100, 0))

"""Задание 3.5"""

# def add_mark(name, mark, journal=None):
#    # Добавьте здесь проверку аргумента mark
#     if mark not in [2,3,4,5]:
#         raise ValueError('Invalid Mark!')
#     if journal is None:
#         journal = {}
#     journal[name] = mark
#     return journal


# phone = "iphone"
# phone_char_list = [i for i in phone]
#
# print(phone_char_list)

# def mean(*numbers):
#     # С помощью встроенной функции isinstance
#     # проверим, что numbers — это tuple
#     print(type(numbers))
#     # Напечатаем содержимое объекта numbers
#     print(numbers)
#     result = sum(numbers) / len(numbers)
#     return result
#
#
# print(mean(5, 4, 4, 3))

'''Напишите функцию mult, которая считает произведение переданных в неё чисел через запятую.

Особое указание: посчитайте результат с использованием цикла for.

После создания функции воспользуйтесь следующим кодом для самопроверки:

print(mult(3,5,10))'''

# def mult(*numbers):
#     print(numbers)
#     print(type(numbers))
#
#     res = 0
#     for i in numbers:
#         print(f"i = {i}")
#         if res == 0:
#             res += i
#         else:
#             res = res * i
#             print (res)
#     return res
#
#
# print(mult(3, 5, 10))


# langs = ['Python', 'SQL', 'Machine Learning', 'Statistics']
# print(langs)
# print(*langs, sep=', ')


'''ЗАДАНИЕ 5.3 (НА САМОПРОВЕРКУ)

Создайте список оценок студента:

marks = [4,5,5,5,5,3,4,4,5,4,5] Передайте в функцию mean_mark, которая была создана в начале данного подраздела 
юнита, этот список, а также фамилию студента Kuznetsov с помощью оператора распаковки. 

Функция mean_mark продублирована:

def mean_mark(name, *marks):
    result = sum(marks) / len(marks)
    # Не возвращаем результат, а печатаем его
    print(name+':', result)'''

# def mean_mark(name, *marks):
#     result = sum(marks) / len(marks)
#     # Не возвращаем результат, а печатаем его
#     print(name+':', result)
# mean_mark ('Mark', 4, 5, 5, 5, 5, 3, 4, 4, 5, 4, 5)

# def print_lists(*kwargs, sep=' ', end='\n'):
#     for i in kwargs:
#         print (*i, sep=sep, end=end)
#         # print(f'i = {i}, type i is {type(i)}\n')
#
#
#
# print_lists([1, 2, 3], [4, 5, 6], [7, 8, 9])
# # 1 2 3
# # 4 5 6
# # 7 8 9
#
# print_lists([1, 2, 3], [4, 5, 6], [7, 8, 9], sep=', ', end='; ')
# # 1, 2, 3; 4, 5, 6; 7, 8, 9;
#
# is_even = lambda num: '4eTHoe' if num % 2 == 0 \
#     else 'He4eTHoe'
# print(is_even(25))
# print(is_even(20))


'''Напишите lambda-функцию для расчёта гипотенузы прямоугольного треугольника: она принимает на вход длины двух 
катетов и возвращает длину гипотенузы (третьей, самой длинной стороны прямоугольного треугольника). 
c = (a**\ 2 + b**\ 2 ) ** (1/2)
Формула: , где  и  — длины катетов,  — длина гипотенузы. Сохраните эту функцию в переменную hyp.'''

# hyp = lambda a, b: (a ** 2 + b ** 2) ** (1 / 2)
#
# print(hyp(3, 4))
# print(hyp(1, 9))


'''Напишите функцию sort_sides, которая сортирует переданный в неё список.
Входной список состоит из кортежей с парами чисел — длинами катетов прямоугольных треугольников.
Функция должна возвращать список, отсортированный по возрастанию длин гипотенуз треугольников.
Примечание: вам пригодится lambda-функция из предыдущего задания. При этом вам потребуется заменить lambda от 2 
аргументов на lamba от одного аргумента и обращаться к элементам кортежа уже при вычислении гипотенузы. 
Пример работы функции:

print(sort_sides([(3,4), (1,2), (10,10)]))
# [(1, 2), (3, 4), (10, 10)]'''

# def sort_sides(l_in):
#     l_in.sort(key=lambda n: (n[0] ** 2 + n[1] ** 2) ** (1/2))
#     return l_in
# print(sort_sides([(3,4), (1,2), (10,10)]))


# print(sort_sides([(3,4), (1,2), (10,10)]))

'''Напишите функцию get_less, которая принимает на вход через запятую список, состоящий из чисел, и ещё одно число. 

Функция должна вернуть первое найденное число из списка, которое меньше переданного во втором аргументе. Если такого 
числа нет, необходимо вернуть None. 

Пример:

l = [1, 5, 8,  10]
print(get_less(l, 8))
# 1
 
print(get_less(l, 0))
# None'''

#
# def get_less(list_in, num):
#     for x in list_in:
#         # print(f'IKS RAVEN {x}')
#         if x < num:
#             return (x)
#     return None
#
#
# l = [1, 5, 8, 10]
# print(get_less(l, 8))
# print(get_less(l, 0))


'''
ЗАДАНИЕ 7.10 (ВЫПОЛНЯЕТСЯ В CODEBOARD НИЖЕ)


Напишите функцию split_date(date), которая принимает на вход строку, задающую дату, в формате ддммгггг без 
разделителей. Функция должна вернуть кортеж из чисел (int): день, месяц, год. 

Примечание. Здесь вам пригодятся срезы строк.

Пример:

print(split_date("31012019"))
# (31, 1, 2019)'''

#
# def split_date(date):
#     return (int(date[0:2]), int(date[2:4]), int(date[4:8]))
#
#
# print(split_date("31012019"))


'''ЗАДАНИЕ 7.11 (ВЫПОЛНЯЕТСЯ В CODEBOARD НИЖЕ)
Напишите функцию is_prime(num), которая проверяет, является ли число простым.

Функция должна вернуть True, если число простое, иначе — False.

Примечание. Простым называют число, которое делится только на 1 или на само себя без остатка. Число 1 простым не 
является. 

Пример:

print(is_prime(1))
print(is_prime(10))
print(is_prime(13))
# False
# False
# True'''
#
#
# def is_prime(num):
#     if num == 1:
#         return False
#     x = 2
#     while (num % x) != 0:
#         x += 1
#     return x == num
#
#
# print(is_prime(1))
# print(is_prime(10))
# print(is_prime(13))

'''
ЗАДАНИЕ 7.12 (ВЫПОЛНЯЕТСЯ В CODEBOARD НИЖЕ)

?

Напишите функцию between_min_max(...), которая принимает на вход числа через запятую.

Функция возвращает среднее между максимумом и минимумом этих чисел.

Пример:

print(between_min_max(10))
print(between_min_max(1,2,3,4,5))
# 10.0
# 3.0'''
#
# def between_min_max(*nums):
#     return((min(nums)+max(nums)) / 2)
#
#
#
#
#
# print(between_min_max(10))
# print(between_min_max(1, 2, 3, 4, 5))

'''
Задание 7.13
Напишите функцию best_student(...), которая принимает на вход в виде именованных аргументов фамилии студентов и их номера в рейтинге (нагляднее в примере).

Необходимо вернуть фамилию студента с минимальным номером по рейтингу.

Пример:

print(best_student(Tom=12, Mike=3))
print(best_student(Tom=12))
print(best_student(Tom=12, Jerry=1, Jane=2))
# Mike
# Tom
# Jerry'''

# def best_student(**student_list):
#     for a, b in student_list.items():
#         if b == (min(student_list.values())):
#             return a
#
#
#
# print(best_student(Tom=12, Mike=3))
# print(best_student(Tom=12))
# print(best_student(Tom=12, Jerry=1, Jane=2))


# is_palindrom = lambda rever: "yes" if rever == rever[::-1] else "no"
#
# print(is_palindrom('12321'))

'''ЗАДАНИЕ 7.15 (ВЫПОЛНЯЕТСЯ В CODEBOARD НИЖЕ)

?

Напишите lambda-функцию area, которая принимает на вход два числа — стороны прямоугольника — через запятую и 
возвращает площадь прямоугольника. 

Пример:

print(area(12,5))
# 60'''

# area = lambda a,b: a * b

'''ЗАДАНИЕ 7.17 (ВЫПОЛНЯЕТСЯ В CODEBOARD НИЖЕ)

?

Напишите функцию sort_ignore_case, которая принимает на вход список и сортирует его без учёта регистра по алфавиту.

Функция возвращает отсортированный список.

Пример:

print(sort_ignore_case(['Acc', 'abc']))
# ['abc', 'Acc']'''

# def sort_ignore_case(ls):
#     ls.sort(key=lambda x: x.lower())
#     return ls
#
#
# print(sort_ignore_case(['Acc', 'abc']))

'''ЗАДАНИЕ 7.16 (ВЫПОЛНЯЕТСЯ В CODEBOARD НИЖЕ)

?

Перепишите функцию between_min_max из задания 7.12 в lambda-функцию. Функция принимает на вход числа через запятую и 
возвращает одно число — среднее между максимумом и минимумом этих чисел. 

Пример:

print(between_min_max(1,2,3,4,5))
# 3.0'''

# between_min_max = lambda *nums: (min(nums) + max(nums)) / 2
#
# print(between_min_max(10))
# print(between_min_max(1, 2, 3, 4, 5))


'''ЗАДАНИЕ 7.18 (ВЫПОЛНЯЕТСЯ В CODEBOARD НИЖЕ)

?

*Задание повышенной сложности

Напишите функцию exchange(usd, rub, rate), которая может принимать на вход сумму в долларах (usd), сумму в рублях (
rub) и обменный курс (rate). Обменный курс показывает, сколько стоит один доллар. Например, курс 85.46 означает, 
что один доллар стоит 85 рублей и 46 копеек. 

В функцию должно одновременно передавать два аргумента. Если передано менее двух аргументов, должна возникнуть ошибка 
ValueError('Not enough arguments'). Если же передано три аргумента, должна возникнуть ошибка: ValueError('Too many 
arguments'). 

Функция должна находить третий аргумент по двум переданным. Например, если переданы суммы в разных валютах, 
должен возвращаться обменный курс. Если известны сумма в рублях и курс, должна быть получена эквивалентная сумма в 
долларах, аналогично — если передана сумма в долларах и обменный курс. 

Пример:

print(exchange(usd=100, rub=8500))
print(exchange(usd=100, rate=85))
print(exchange(rub=1000, rate=85))
# 85.0
# 8500
# 11.764705882352942
print(exchange(rub=1000, rate=85, usd=90))
# ValueError: Too many arguments
print(exchange(rub=1000))
# ValueError: Not enough arguments'''

# def exchange(usd=None, rub=None, rate=None):
#     if usd is not None and rub is not None and rate is not None:
#         raise ValueError('Too many arguments')
#     if rub is not None:
#         if rate is not None:
#             return rub / rate
#         if usd is not None:
#             return rub / usd
#     if usd is not None:
#         if rate is not None:
#             return usd * rate
#     raise ValueError('Not enough arguments')
#
#
#
#
# print(exchange(usd=100, rub=8500))
# print(exchange(usd=100, rate=85))
# print(exchange(rub=1000, rate=85))
# print(exchange(rub=1000, rate=85, usd=90))
# print(exchange(rub=1000))


# if (9*8)**(1/3) > 7:
#     print("истина")
# else:
#     print ("ложь")

'''Защита от дурака'''
'''Титенков Владимир группа 76 курса Data Science'''

while True:  # для возможности повторного ввода данных запаковываем ввод и проверку в "бесконечный цикл"
    name = input('Введите имя: ')
    if name.isalpha():
        print(f'Принято, Привет {name.capitalize()}!')
        break
    else:
        print(f'Не корректное имя!\nВы ввели "{name}")')

while True:
    birthday = input('Введите дату рождения в формате год-месяц-день: ')
    try:
        year, month, day = birthday.split("-")  # пробуем разобрать строку используя символ разделитель "-" если это
        # не удается, обрабатываем ошибку и начинаем цикл сначала. Если удается приступаем к повторной проверке

        if not (0 < int(year) <= 2021 and 0 < int(month) <= 12 and 0 < int(day) <= 31):  # проверяем диапазоны значений
            raise Exception("")  # искусственно вызываем ошибку если не срабатывает проверка диапазона введенных значений
        print(f'Принято, Год = {year}, месяц = {month}, день = {day}')
        break
    except:
        print(f'Вы некорректно ввели дату, попробуйте еще раз, например: "2021-11-21')

# mail = input('Введите почту: ')
