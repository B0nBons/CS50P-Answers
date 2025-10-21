import sys


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
        sys.exit(0)
    else:
        print("Invalid")
        sys.exit(1)


def is_valid(plate):
    num = False

    if len(plate) < 2 or len(plate) > 6:
        return False

    if not plate[0].isalpha() or not plate[1].isalpha():
        return False

    for let in plate:
        if not let.isalnum():
            return False

    for letter in range(len(plate)):
        if plate[letter].isdigit():
            if plate[letter] == '0' and letter == 2:
                return False
            num = True

        elif num and plate[letter].isalpha():
            return False

    return True


if '__name__' == '__main__':
    main()
