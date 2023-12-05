"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def half_division_number(bounds):
    if bounds[2] == 0:
        return round((bounds[0]+bounds[1]) / 2, 0)
    


def fast_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    bounds = [1, 100, 0]
    while True:
        count += 1
        predict_number = half_division_number(bounds)  # предполагаемое число
        equals = number - predict_number
        if equals == 0:
            break  # выход из цикла если угадали
        if equals < 0:
            bounds[1] = predict_number
        else:
            bounds[0] = predict_number
        bounds[2] = equals       
    return count


def score_game(fast_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(fast_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(fast_predict)
