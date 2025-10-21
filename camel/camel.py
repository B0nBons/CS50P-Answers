camel = input("Enter camelCase: ")
snake = ""

for let in camel: # note to self, don't do len(camel), causes error
    if let.isupper() == True:
        snake += '_' + let.lower()
    elif let.islower() == True:
        snake += let

print("Snake_case = " + str(snake))
