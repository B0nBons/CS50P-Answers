from tabulate import tabulate
import sys

# >>> print(tabulate([["Name","Age"],["Alice",24],["Bob",19]],
# ...                headers="firstrow"))
# Name      Age
# ------  -----
# Alice      24
# Bob        19


try:
    if ".csv" not in sys.argv[1]:
        print("Not a CSV")
        sys.exit(1)
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    if len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    with open(sys.argv[1], 'r') as file:
        lines = file.readlines()
        line_no = 1
        lists = []
    for line in lines:
        if line_no == 1:
            pizza, small, large = line.split(",")
            large = large.replace("\n","" )
            headers = [pizza, small, large]
            lists.append(headers)
            line_no += 1
        elif line_no == 2:
            x, y, z = line.split(",")
            list2 = [x, y, z]
            line_no += 1
        elif line_no == 3:
            x, y, z = line.split(",")
            list3 = [x, y, z]
            line_no += 1
        elif line_no == 4:
            x, y, z = line.split(",")
            list4 = [x, y, z]
            line_no += 1
        elif line_no == 5:
            x, y, z = line.split(",")
            list5 = [x, y, z]
            line_no += 1
        elif line_no == 6:
            x, y, z = line.split(",")
            list6 = [x, y, z]
            line_no += 1

    print(tabulate([headers, list2, list3, list4, list5, list6],headers="firstrow", tablefmt='grid'))

# >>> print(tabulate([["Name","Age"],["Alice",24],["Bob",19]],
# ...                headers="firstrow"))

except ValueError:
    print("Unable to read")
    sys.exit(1)
except FileNotFoundError:
    print("File not found")
    sys.exit(1)
