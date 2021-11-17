# import numpy as np
#
#
# def random_predict(number: int = 1) -> int:
#     """Угадываем число
#     Args:
#         number (int, optional): Загаданное число. Defaults to 1.
#     Returns:
#         int: Число попыток"""
#     count = 0
#     lower_border = 1
#     upper_border = 100
#     predict_number = np.random.randint(1, 101)
#     while True:
#         count += 1
#         if number > predict_number:
#             lower_border = predict_number
#         elif number < predict_number:
#             upper_border = predict_number
#         round(lower_border + upper_border) / 2
#         return count
#
#
# def score_game(random_predict) -> int:
#     """За какое количство попыток в среднем за 10000 подходов угадывает наш алгоритм
#     Args:
#         random_predict ([type]): функция угадывания
#     Returns:
#         int: среднее количество попыток
#     """
#     count_ls = []
#     np.random.seed(1)  # фиксируем сид для воспроизводимости
#     random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел
#     for number in random_array:
#         count_ls.append(random_predict(number))
#     score = int(np.mean(count_ls))
#     print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
#     return score
#
#
# if __name__ == "__main__":
#     # RUN
#     score_game(random_predict)


# from random import randint
#
# m, n, y, z = [int(input(i)) for i in ("m = ", "n = ", "y = ", "z = ")]
# matrix = [[randint(y, z) for _ in range(n)] for j in range(m)]
# print('матрица')
# for i in matrix:
#     print(*i)
#
# print(' \nминимальны значения строк\n')
#
# for x in range(m):
#     print(x + 1, 'строка', 'минимальное', min(matrix[x]))
#
# print(' \nминимальны значения столбцов\n')
#
# for x in range(n):
#     list_val_col = [matrix[i][x] for i in range(m)]
#     print(x + 1, 'столбец', 'минимальное', min(list_val_col))
n = 0
while n > 1:
    if n == 1:
        return True
    elif n % 2 == 0:
        n = n / 2
    elif n % 2 == 1:
        n = (n * 3 + 1) / 2
return False