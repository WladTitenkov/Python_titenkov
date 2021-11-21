"""Защита от дурака"""
'''Титенков Владимир группа 76 курса Data Science'''

while True:  # для возможности повторного ввода данных запаковываем ввод и проверку в "бесконечный цикл"
    name = input('Введите имя: ')
    if name.isalpha():
        print("\n" * 100)
        print(f'Принято, Привет {name.capitalize()}!')
        break
    else:
        print(f'Не корректное имя!\nВы ввели "{name}"')

while True:
    birthday = input('Введите дату рождения в формате год-месяц-день: ')
    try:
        year, month, day = birthday.split("-")  # пробуем разобрать строку используя символ разделитель "-" если это
        # не удается, обрабатываем ошибку и начинаем цикл сначала. Если удается приступаем к повторной проверке

        if not (0 < int(year) <= 2021 and 0 < int(month) <= 12 and 0 < int(day) <= 31):  # проверяем диапазоны значений
            raise Exception("")  # искусственно вызываем ошибку если не срабатывает проверка диапазона введенных
            # значений
        print("\n" * 100)
        print(f'Принято, Год = {year}, месяц = {month}, день = {day}')
        break
    except:
        print(f'Вы некорректно ввели дату, попробуйте еще раз, например: "2021-11-21"')

while True:  # проверим почту на наличие строго одного символа "@" и хотя бы одной точки после символа "@". Это не
    # полная проверка правильности адреса электронной почты но в 90% случаев этого вполне достаточно
    mail = input('Введите почту: ')
    at_index = mail.find("@")  # присваиваем переменной индекс позиции символа "@", если символа нет, то -1
    at_count = mail.count("@")
    point_index = mail.find(".", at_index)  # тут ищем символ "." после символа "@" (вдруг у нас в левой части есть
    # точка как у меня (titenkov.vova@gmail.com)
    if at_index != -1 and point_index != -1 and at_count == 1:
        print("\n" * 100)
        print(f'Введенный адрес похож на настоящий\nвы ввели: "{mail}"\n')
        break
    else:
        print(f'Вы ввели некорректный адрес, попробуйте еще раз\n')

# покопавшись в интернетах нашел крутой модуль для проверки корректности email. Там даже можно проверять доступность
# SMTP сервера у домена и даже наличия конкретного адреса электронной почты

from validate_email import validate_email

while True:
    mail2 = input('Введите вторую почту: ')
    valid_chek = validate_email(mail2)
    if valid_chek:
        print("\n" * 100)
        print(f'Введенный адрес ОЧЕНЬ похож на настоящий\nвы ввели: "{mail2}"')
        break
    else:
        print(f'Вы ввели некорректный адрес, попробуйте еще раз\n')

print(f'\nГотово! Спасибо, {name.capitalize()}! Напоминаю, вы ввели:'
      f'\nДата: Год = {year}, месяц = {month}, день = {day}\n'
      f'Адрес e-mail: {mail}\n'
      f'Второй адрес e-mail: {mail2}')
