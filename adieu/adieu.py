import inflect
import sys

p = inflect.engine()

names = []


while True:
    try:
        name = input("").title()
        names.append(name)
    except EOFError:
        if len(names) == 1:
            print("Adieu, adieu, to " + name)
            sys.exit()
        elif len(names) == 2:
            print("Adieu, adieu, to " + names[0] + " and " + names[1])
            sys.exit()
        else:
            fin = print("Adieu, adieu, to", p.join((names)))
            sys.exit()
