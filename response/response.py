from validator_collection import validators, checkers, errors


def main():
    if is_valid(input("Enter email: ")):
        print("Valid")
    else:
        print("Invalid")

def is_valid(email):
     yesorno = checkers.is_email(email)
     return yesorno

if __name__ == '__main__':
    main()
