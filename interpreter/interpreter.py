math = input("enter math problem, spaced out: ")
x, y, z = math.split(" ")

x = float(x)
z = float(z)

if y == "+":
    product = x+z
    print(product)
elif y == "-":
    product = x-z
    print(product)
elif y == "*":
    product = x*z
    print(product)
elif y == "/":
    product = x/z
    print(product)
else:
    print("??")
