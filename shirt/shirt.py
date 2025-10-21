import sys
from PIL import Image
from PIL import ImageOps
from os.path import splitext

def main():
    if valid(sys.argv):
        shirtify(sys.argv[1], sys.argv[2])

def valid(a):
    if len(a) < 3:
        print("Too few command-line arguments")
        sys.exit(1)

    if len(a) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

    allowed = [".jpeg", ".png", ".jpg"]
    inp = splitext(a[1])
    out = splitext(a[2])
    inp = inp[1].lower()
    out = out[1].lower()
    if inp not in allowed:
        print("Invalid input")
        sys.exit(1)

    if out not in allowed:
        print("Invalid output")
        sys.exit(1)

    if inp != out:
        print("Input and Output file extensions don't match")
        sys.exit(1)
    else:
        return True

def shirtify(inp, out):
    try:
        with Image.open("shirt.png") as shirt:
            with Image.open(inp) as image:
                image = ImageOps.fit(image, shirt.size)
                image.paste(shirt, shirt)
                image.save(out)
                sys.exit(0)

    except FileNotFoundError:
        print("Input doesn't exist")
        sys.exit(1)
    except OSError:
        print("Can not convert " + inp)
        sys.exit(1)


if __name__ == "__main__":
    main()

