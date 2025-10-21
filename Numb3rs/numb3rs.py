import re
import sys

# formatted in dot-decimal notation as #.#.#.#.
# But each # should be a number between 0 and 255, inclusive.
def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        first, second, third, fourth = ip.split(".")
        if int(first)  > 255:
            return False
        if int(second) > 255:
            return False
        if int(third) > 255:
            return False
        if int(fourth) > 255:
            return False
        else:
            return True
    except ValueError:
        return False

if __name__ == "__main__":
    main()
