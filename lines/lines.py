import sys

try:

    counter = 0
    f = sys.argv[1]

    if len(sys.argv) >= 3:
        print("Too many command-line arguments")
        sys.exit(1)

    elif ".py" not in sys.argv[1]:
        print("Not a Python file")
        sys.exit(1)

    with open(f, "r") as file:
        for line in file:
            if not (line.lstrip().startswith("#") or line.strip() == ""):
                counter += 1

    print(counter)
    sys.exit(0)

except IndexError:
    print("Too few command-line arguments")
    sys.exit(1)

except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)
