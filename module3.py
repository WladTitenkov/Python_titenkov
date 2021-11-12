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

'''Условие задачи. Найти сумму всех натуральных чисел от 1 до N включительно.'''

# n = input('Enter number: ')
# n = range(1, int(n) + 1)
# print(n)
# sum = 0
# for i in n:
#     sum = sum + i
#     print (f'{sum-i}+{i}={sum}')


