import re
import sys

# <iframe src="https://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
# http://youtube.com/embed/xvFZjo5PgG0
# https://youtube.com/embed/xvFZjo5PgG0
# https://www.youtube.com/embed/xvFZjo5PgG0

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if link := re.search(r"<iframe src=\"https?://(www\.)?youtube\.com/embed/([a-zA-Z0-9]+)\"></iframe>", s):
        x = "https://youtu.be/" + link.group(2)
        return x
    else:
        return None


if __name__ == "__main__":
    main()
