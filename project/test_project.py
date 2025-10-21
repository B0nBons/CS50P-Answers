import pytest
from project import makedeck, difficulty, colour

# Test cases for makedeck()
def test_makedeck():
    deck = makedeck()
    # Check the deck contains 52 cards
    assert len(deck) == 52

    # Check there are no duplicate cards
    unique_cards = set(tuple(card) for card in deck)
    assert len(unique_cards) == 52

    # Check suits and values
    suits = {"Hearts", "Diamonds", "Clubs", "Spades"}
    values = {"Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"}
    for card in deck:
        assert card[0] in values, f"Invalid card value: {card[0]}"
        assert card[1] in suits, f"Invalid card suit: {card[1]}"

# Test cases for difficulty()
# Test cases for difficulty()
def test_difficulty():
    # Test valid inputs
    assert difficulty(inp="1") == 1, "Expected difficulty to be 1"
    assert difficulty(inp="2") == 2, "Expected difficulty to be 2"
    assert difficulty(inp="3") == 3, "Expected difficulty to be 3"

    # Test invalid input: should assign random difficulty
    random_difficulty = difficulty(inp="invalid")
    assert random_difficulty in [1, 2, 3], "Random difficulty assignment failed for invalid input."


# Test cases for colour()
def test_colour():
    text = "Test String"
    colored_text = colour(text)
    # Check that the color codes are added correctly
    assert "\u001b[31m" in colored_text
    assert "\u001b[30m" in colored_text
    assert text in colored_text
