food = [
    "Baja Taco",
    "Burrito",
    "Bowl",
    "Nachos",
    "Quesadilla",
    "Super Burrito",
    "Super Quesadilla",
    "Taco",
    "Tortilla Salad"]
price = [
    4.25,
    7.50,
    8.50,
    11.00,
    8.50,
    8.50,
    9.50,
    3.00,
    8.00
]
total = 0
while True:
    try:
        item = input("Item: ")
        item = item.title()
        if item in food:
            index = food.index(item)
            cost = price[index]
            total += cost
            final =  f"{total:.2f}"
            print(f"\nTotal: ${final}")

    except EOFError:
            final =  f"{total:.2f}"
            print(f"\nTotal: ${final}")
            exit()
