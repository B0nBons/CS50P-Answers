def main():
    frac = input("Fraction: ")
    x = convert(frac)
    print(gauge(x))

def convert(frac):
    num, den = frac.split("/")
    if int(den) == 0:
        raise ZeroDivisionError
    elif int(num)/int(den) > 1:
        raise ValueError
    else:
        return int(int(num)/int(den) * 100)

def gauge(percentage):
    if 0 <= percentage <= 1:
        return "E"
    elif 99 <= percentage <= 100:
        return "F"
    else:
        return f"{int(percentage)}%"

if __name__ == "__main__":
    main()
