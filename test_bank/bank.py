import sys
def main():
    greet = input("Enter Greeting: ")
    greet = greet.lower()
    print("$" + str(value(greet)))
    exit(0)
def value(greet):
    greet = greet.lower()
    if greet.startswith("hello"):
        return 0
    elif greet.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()

