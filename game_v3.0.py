'''Компьютер пытается угадать число менее, чем за 10 попыток'''
import random

guess = int(input("Выберите число, которое вы хотите, чтобы компьютер угадал от 1 до 100: "))

turns = 0
a = None

compguess = random.randint(1,100)

while turns < 10 and 100 > guess >= 1 and compguess != guess: #компьютер имеет 10 ходов, чтобы угадать число, вы можете изменить его на то, что хотите
    print("Предположение компьютера:  ", compguess)
    if compguess>guess:
        a = compguess
        compguess = random.randint(1, compguess)

    elif compguess < guess:
        compguess = random.randint(compguess, a)
        turns += 1


    if compguess == guess and turns < 10:
        print("Компьютер угадал ваше число: ", guess)
        turns += 1

    elif turns >= 10 and compguess != guess:
        print("Компьютер не смог угадать ваш номер, молодец.")


input("")
