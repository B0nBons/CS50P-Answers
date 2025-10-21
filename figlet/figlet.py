from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

fontlist = figlet.getFonts()
def main():
    try:
        if len(sys.argv) == 1:
            fonto = random.choice(fontlist)
            figlet.setFont(font=fonto)
            words = input ("")
            print(figlet.renderText(words))
            sys.exit()
        elif "-f" == sys.argv[1] or "--font" == sys.argv[1]:
            figlet.setFont(font=sys.argv[2])
            words = input("")
            print(figlet.renderText(words))
            sys.exit()
        elif len(sys.argv) == 2:
            print("Invalid Usage")
            sys.exit(1)
        else:
            print("Invalid Usage")
            sys.exit(1)


    except IndexError:
        print("Invalid Usage")
        sys.exit(1)
main()
sys.exit(1)
