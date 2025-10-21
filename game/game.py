import random
string = "wow"
def game():
    while True:
        try:
            level = input("Level: ")
            level = round(int(level))
            while int(level) < 0 or level == type(string) == str:
                level = input("Level: ")
            secret = random.randint(1, level)
            guess = "hello"
            while guess != secret:
                guess = input("Guess: ")
                if int(guess) > secret:
                    print("Too Large!" )
                elif int(guess) < secret:
                    print("Too small!")
                if int(guess) == secret:
                    print("Just Right!")
                    exit()
        except ValueError:
            pass
        except TypeError:
            pass

game()
