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

sum = 0
n = 1
while sum < 500:
    print(n, end = "\t - \t"); print (f'{sum} + {n} = {sum+n}')
    sum += n
    n +=1
print (sum)

