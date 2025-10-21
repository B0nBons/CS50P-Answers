user = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
lower = user.lower()

if user == "42":
    print("Yes")
elif user == "forty-two":
    print("Yes")
elif user == "forty two":
    print("Yes")
elif lower == "forty two":
    print("Yes")
elif " " in user:
    if "42" in user:
        print("Yes")
else:
    print("No")
