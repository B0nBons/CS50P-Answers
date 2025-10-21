def main():
    global vowels
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    print(shorten(word))

def shorten(word = "yay"):
    vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    word = input("Input: ")
    for letter in word:
        if letter in vowels:
            word = word.replace(letter, "")

    return word.lower()

if __name__ == "__main__":
    main()



