'''Компьютер угадывет число за 7 попыток'''

def computer_guess(num):
    low = 1
    high = 100
    guess = (low+high)//2
    while guess != num:
        guess = (low+high)//2
        print("The computer takes a guess...", guess)
        if guess > num:
            high = guess
        elif guess < num:
            low = guess + 1

    print("The computer guessed", guess, "and it was correct!")


def main():
    num = int(input("Enter a number: "))
    if num < 1 or num > 100:
        print("Must be in range [1, 100]")
    else:
        computer_guess(num)
if __name__ == '__main__':
    main()    