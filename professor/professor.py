import random
import sys


allowed = [1, 2, 3]
def main():
    level = get_level()
    total_fails = 0
    for i in range(10):
        x, y, fin = gen_int(level, x = 0, y = 0, fin = 0)
        ans = input(str(x)+ " + " + str(y) + " = ")
        if ans != fin:
            print("EEE")
            ans = input(str(x)+ " + " + str(y) + " = ")
        if ans != fin:
            print("EEE")
            ans = input(str(x)+ " + " + str(y) + " = ")
        if ans != fin:
            print("EEE")
            print(str(x) + " + " + str(y) + " = " + fin)
            total_fails += 1
    print("Score: " + str(10-total_fails))
    sys.exit()

def get_level(level = 0):
    level = 0
    while True:
        try:
            while int(level) not in allowed:
                level = input("Level: ")
            return int(level)
        except ValueError:
            pass

def gen_int(level, x = 0, y = 0, fin = 0):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
        fin = x + y
        fin = str(fin)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
        fin = x + y
        fin = str(fin)
    elif level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
        fin = x + y
        fin = str(fin)
    return x, y, fin

if __name__ == "__main__":
    main()
    sys.exit()
