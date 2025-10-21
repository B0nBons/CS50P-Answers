def fin():
    ans = frac("Enter the frac: ")
    print(ans)


def frac(words):
    while True:
        try:
            words = input(words)
            numerator, denominator = words.split("/")
            if 0 <= int(numerator)/int(denominator) <= 0.1:
                return ("E")
            elif 0.9 <= int(numerator)/int(denominator) <= 1:
                return ("F")
            elif 0.1 < int(numerator)/int(denominator) < 0.9:
                return str(round(int(numerator)/int(denominator)*100)) + "%"
        except (ValueError):
            pass
        except (ZeroDivisionError):
            pass


fin()
