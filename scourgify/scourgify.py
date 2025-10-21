import sys
import csv

def main():
    if valid(sys.argv):
        make_csv(sys.argv[1], sys.argv[2])

def valid(argv):
    if len(argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    if ".csv" not in argv[1]:
        print("Couldn't read " + argv[1])
        sys.exit(1)

    return True

def make_csv(input, output):
    try:
        with open(input) as csvfile:
            lines = csv.DictReader(csvfile)
            with open(output, "w", newline="") as new_file:
                fieldnames = ["first", "last", "house"]
                writer = csv.DictWriter(new_file, fieldnames=fieldnames)
                writer.writeheader()
                for row in lines:
                    name = row["name"].replace("\"", "").split(",")
                    a = name[1].strip()
                    b = name[0].strip()
                    home = row["house"].strip()
                    writer.writerow({"first": a, "last": b, "house": home })
    except FileNotFoundError:
        print("Could not read " + argv[1])
        sys.exit(1)

if __name__ == "__main__":
    main()
