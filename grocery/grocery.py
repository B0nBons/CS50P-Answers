shopping = []
times    = []

while True:
    try:
        item = input("")
        item = item.upper()
        if item in shopping:
            index = shopping.index(item)
            total = times[index]
            total += 1
            times[index] = (total)
        if item not in shopping:
            shopping.append(item)
            shopping.sort()
            shopping.index(item)
            times.append(1)

    except EOFError:
        for i in range(len(times)):
            print(str(times[i]) + " " + str(shopping[i]))
        exit()
