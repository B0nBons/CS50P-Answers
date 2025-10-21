import random as r
from colorama import Fore as f
from tabulate import tabulate as tb
# Import libraries


# Define classes
class Dealer:
    def __init__(self, difficulty):
        self.diff = difficulty
        # Ony needed for play func, so it knows when to stand
        self.hand = []
        # Hand is set to an empty list

    def __str__(self):
        return f"Dealer difficulty is {self.diff}"
        # Shouldn't be returned as a str in any case

    def deal_card(self, deck):
        index = r.randint(0, len(deck) - 1)
        return deck.pop(index)
        # When dealing, choose a random card based on the length of the deck

    def play(self, deck):
        # Dealer's strategy based on difficulty, higher risk, higher reward
        while self.calculate_points() < 17 + self.diff:
            self.hand.append(self.deal_card(deck))
            # Add a random card from the deck

    def calculate_points(self):
        points = 0
        aces = 0
        # Aces are counted seperatly, as they have a differing value
        for card in self.hand:
            if card[0] in ['Jack', 'Queen', 'King']:
                points += 10
            elif card[0] == 'Ace':
                aces += 1
                points += 11
            else:
                points += int(card[0])

        while points > 21 and aces:
            points -= 10
            aces -= 1
            # If the ace makes the hand > 21, remove it

        return points

        # Onyl show hand if the player has drawn
    def show_hand(self, reveal=False):
        if reveal:
            return f"Dealer's hand:\n{self.format_hand(self.hand)}\n({self.calculate_points()} points)"
        else:
            return f"Dealer's hand:\n{self.format_hand([self.hand[0]])}\n('Hidden')"

        # Makes the cards print pretty
    def format_hand(self, hand):
        card_art = ""
        for card in hand:
            value = card[0][0] if card[0] != '10' else '10'
            suit = card[1][0].lower()
            heart = chr(9829) # '♥'
            diamond = chr(9830) # '♦'
            spade = chr(9824) # '♠'
            club = chr(9827) # '♣'
            # Print the cards nicely
            if suit[0] == "h":
                card_art += f" _____ \n"
                card_art += f"|{value:<2}   |\n"
                card_art += f"|  {heart}  |\n"
                card_art += f"|   {value:>2}|\n"
                card_art += f" ----- \n"
                # Heart card
            if suit[0] == "d":
                card_art += f" _____ \n"
                card_art += f"|{value:<2}   |\n"
                card_art += f"|  {diamond}  |\n"
                card_art += f"|   {value:>2}|\n"
                card_art += f" ----- \n"
                # Diamond card
            if suit[0] == "s":
                card_art += f" _____ \n"
                card_art += f"|{value:<2}   |\n"
                card_art += f"|  {spade}  |\n"
                card_art += f"|   {value:>2}|\n"
                card_art += f" ----- \n"
                # Spade card
            if suit[0] == "c":
                card_art += f" _____ \n"
                card_art += f"|{value:<2}   |\n"
                card_art += f"|  {club}  |\n"
                card_art += f"|   {value:>2}|\n"
                card_art += f" ----- \n"
                # Club card
        return card_art

class Player:
    def __init__(self):
        self.hand = []
        # Player starts with an empty hand

    def hit(self, deck):
        self.hand.append(deck.pop(r.randint(0, len(deck) - 1)))
        # If a hit, adds one to their hand, removes the card from deck

    def calculate_points(self):
        points = 0
        aces = 0
        # Follows same scoring as dealer
        for card in self.hand:
            if card[0] in ['Jack', 'Queen', 'King']:
                points += 10
            elif card[0] == 'Ace':
                aces += 1
                points += 11
            else:
                points += int(card[0])

        while points > 21 and aces:
            points -= 10
            aces -= 1

        return points

    def show_hand(self):
        # Player will always be able to see their own hand
        return f"Player's hand:\n{self.format_hand(self.hand)}\n({self.calculate_points()} points)"

    def is_bust(self):
        # Returns True or False
        return self.calculate_points() > 21

    def has_blackjack(self):
        # If player has a blackjack, returns True
        return self.calculate_points() == 21

    def format_hand(self, hand):
        card_art = ""
        for card in hand:
            value = card[0][0] if card[0] != '10' else '10'
            suit = card[1][0].lower()
            heart = chr(9829) # '♥'
            diamond = chr(9830) # '♦'
            spade = chr(9824) # '♠'
            club = chr(9827) # '♣'

            if suit[0] == "h":
                card_art += f" _____ \n"
                card_art += f"|{value:<2}   |\n"
                card_art += f"|  {heart}  |\n"
                card_art += f"|   {value:>2}|\n"
                card_art += f" ----- \n"
            if suit[0] == "d":
                card_art += f" _____ \n"
                card_art += f"|{value:<2}   |\n"
                card_art += f"|  {diamond}  |\n"
                card_art += f"|   {value:>2}|\n"
                card_art += f" ----- \n"
            if suit[0] == "s":
                card_art += f" _____ \n"
                card_art += f"|{value:<2}   |\n"
                card_art += f"|  {spade}  |\n"
                card_art += f"|   {value:>2}|\n"
                card_art += f" ----- \n"
            if suit[0] == "c":
                card_art += f" _____ \n"
                card_art += f"|{value:<2}   |\n"
                card_art += f"|  {club}  |\n"
                card_art += f"|   {value:>2}|\n"
                card_art += f" ----- \n"
        return card_art

def difficulty(inp=None):
    try:
        if inp is None:
            print(tb([['Difficulty', 'Select'], ['Hard', 1], ['Medium', 2],
                       ['Easy', 3]], headers="firstrow", tablefmt="outline"))
            inp = input("Select difficulty: ").strip()

        x = int(inp)
        if 0 >= x or x > 3:
            raise ValueError
        print("Difficulty has been set to " + str(x))
        return x

    except ValueError:
        x = r.randint(1, 3)
        print("Difficulty has been set to: " + str(x))
        return x


def colour(str):
    # Colour
    red = f.RED
    bl = f.BLACK
    return red + str + bl

def makedeck():
    cat = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    list = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    return [[card, category] for category in cat for card in list]
    # Create the list, with one card of each number of each suite

def main():
    print(f.BLACK + "Welcome to ♠♣Black"+f.RED + "jack!♥♦" + f.BLACK)
    # Custom colour an intro message
    while True:
        deck = makedeck()
        r.shuffle(deck)
        # Randomize deck order
        dealer = Dealer(difficulty())
        player = Player()
        # Start off with 2 cards
        for i in range(2):
            player.hit(deck)
            dealer.hand.append(dealer.deal_card(deck))

        print(player.show_hand())
        print(dealer.show_hand())

        # Player's turn
        while True:
            if player.has_blackjack():
                print(colour("Blackjack! You win!"))
                return
        # Keep playing until somebody wins, stands or goes bust
            choice = input("Choose: [H]it, [S]tand: ").strip().lower()
            if choice == 'h':
                player.hit(deck)
                print(player.show_hand())
                # Print the new hand
                if player.is_bust():
                    print(colour("Bust! You lose!"))
                    return
            elif choice == 's':
                break
            else:
                print(colour("Invalid choice. Please choose again."))

        # Dealer's turn
        dealer.play(deck)
        print(dealer.show_hand(reveal=True))

        # Compare hands
        player_points = player.calculate_points()
        dealer_points = dealer.calculate_points()

        # 21 Points to win
        if dealer_points > 21 or player_points > dealer_points:
            print("You win!")
        elif player_points < dealer_points:
            print("Dealer wins!")
        else:
            print("It's a tie!")

        # Play again?
        if input(colour("Play again? (y/n): ")).strip().lower() != 'y':
            break


if __name__ == '__main__':
    main()
