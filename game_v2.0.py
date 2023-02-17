"""Угадай число"""
"компьютер сам загадывает и сам угадывает число"

import numpy as np
from numpy.core.fromnumeric import mean
from numpy.lib.function_base import append
from numpy.random.mtrand import randint, random

def random_predict(number: int = 1) ->int:
    
    count = 0
    while True:
        count+= 1
        predict_number = np.random.randint(1,101) # Предполагаемое число
        if number == predict_number:
            break #конец игры. Выход из цикла. 
    return(count)

def score_game(random_predict) -> int:
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1,101, size=(1000)) # Загадываем список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    score = int(np.mean(count_ls))
    print(f"Алгоритм угадыввает число в среднем за: {score} попыток")

    return(score)

score_game(random_predict)