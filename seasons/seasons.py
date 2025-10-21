from datetime import date
import inflect
import sys


def get_mins(birth_date, today):
    return (today - birth_date).days * 24 * 60


def main():
    try:
        birth_date = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid input.")

    total_minutes = get_mins(birth_date, date.today())
    i = inflect.engine()
    print(f"{i.number_to_words(total_minutes, andword='').capitalize()} {i.plural('minute', total_minutes)}")


if __name__ == "__main__":
    main()
