import random


class RangeError(Exception):
    pass


low = 1
high = 50


def restart():

    try:
        print("\n press 1 to restart \n press 0 to leave")
        restart_ = int(input())
        if restart_ == 1:
            return True
        elif restart_ == 0:
            return False
        else:
            return restart()
    except ValueError:
        return restart()


start = True
while start:
    correct_answer = random.randint(low, high)
    n = 5
    while n > 0:

        try:
            print("!!! {} chances left to guess the number  !!!".format(n))
            n = n - 1

            guess_num = int(input("Guess any number from {} to {}: ".format(low, high)))
            if guess_num < low or guess_num > high:
                raise RangeError

            if correct_answer == guess_num:
                print(" !!!--- You Win ----!!!")
                break
            elif correct_answer > guess_num:
                print(" Correct answer is greater!")
            elif correct_answer < guess_num:
                print("Correct answer is smaller!")

        except ValueError:
            print("Your guess isn't valid input.")
        except RangeError:
            print("Your guess is out of bound !!.")

    if n == 0:
        print("You lose!")
    start = restart()









