fruit = ["apple", "avocado", "banana", "cantaloupe", "grapefruit", "grapes", "honeydew", "kiwifruit", "lemon", "lime",
          "nectarine","orange", "peach", "pear", "pineapple", "plum", "strawberries", "sweet cherries", "tangerine", "watermelon"]
calri = [130,        50,        110,       50,           60,          90,        50,       90,     15,      20,
               60,       80,       60,     100,       50,        70,       50,            100,         50,         80]

what = input("What fruit? ")
what = what.lower()

for fr in range(len(fruit)):
    if fruit[fr] == what:
        print("Calories: " + str(calri[fr]))
        break
