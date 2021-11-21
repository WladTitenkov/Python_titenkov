"""Шахматная доска"""
'''Титенков Владимир группа 76 курса Data Science'''

x_current = 1
y_current = 7
print(f'Координаты ферзя ({x_current},{y_current}), куда вы хотите переместить фигуру?')
x_new = int(input("Введите координату X: "))
y_new = int(input("Введите координату Y: "))

if 1<=int(x_new)<=9 and 1<=int(y_new)<=9:
    if abs(x_current - int(x_new)) == abs(y_current - int(y_new)) :
        print('Успешный ход')
    elif x_current == int(x_new):
        print('Успешный ход')
    elif y_current == int(y_new):
        print('Успешный ход')
    else:
        print('Неуспешный ход')
else:
    print('Неуспешный ход, координаты за пределами доски')
print('Выполнена попытка переместить ферзя из клетки:', (x_current, y_current), 'в клетку:', (x_new, y_new))