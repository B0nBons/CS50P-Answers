def main():
    time = input("What time is it? ")
    if 7 <= convert(time) and convert(time)<= 8:
        print("breakfast time")
    elif 12 <= convert(time) and convert(time) <= 13:
        print("lunch time")
    elif 18 <= convert(time) and convert(time)<= 19:
        print("dinner time")
    else:
        pass


def convert(time):
    x, y = time.split(":")
    hour = float(x)
    minute = float(y) * 1 / 60
    return float(hour+minute)


if __name__ == "__main__":
    main()
