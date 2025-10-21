import re
import sys

def main():
    print(count(input("Text: ")))
    sys.exit(0)

def count(str):
    str = str.lower()
    x = re.findall("(^|\W)um($|\W)", str, re.IGNORECASE)
    return len(x)

if __name__ == "__main__":
    main()
