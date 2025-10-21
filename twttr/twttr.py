vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]

word = input("Input: ")

for letter in word:
    if letter in vowels:
        word = word.replace(letter, "")
print("Output: " + word)
