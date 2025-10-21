# Blackjack Simulator
#### Video Demo:  <https://www.youtube.com/watch?v=Vjgj_7PDMIg>

#### Description:
My project, **Blackjack Simulator** is a Python-based command-line game that replicates the experience of playing blackjack. The game provides an interactive environment where players can compete against a dealer with varying difficulty levels. This project includes a dynamic game flow, visually appealing card representations, and adherence to the rules of blackjack.

The project implements the core features of blackjack:
- Card dealing and shuffling.
- Player actions: hit or stand.
- Dealer actions based on difficulty levels.
- Scoring system, including handling Aces as 1 or 11.
- Bust, tie, win, and lose conditions.

The dealer's difficulty influences their strategy, with higher difficulty levels making them more likely to play aggressively. The player's objective is to beat the dealer without exceeding 21 points.

#### Features:
- **Dynamic Gameplay:** Players can choose to hit or stand based on their hand's score.
- **Dealer AI:** The dealer follows a strategy influenced by the chosen difficulty level.
- **Replayability:** Players can replay the game (until they lose)

#### File Structure:
- **`project.py`:**
  - The main file that houses the `main()` function, the `Dealer` and `Player` classes, and utility functions.
  - Implements the game loop and player-dealer interactions.
  - Contains the following primary functions:
    - `makedeck()`: Creates and returns a deck of cards.
    - `difficulty()`: Allows the player to select the dealer's difficulty level.
    - `colour()`: Adds color to strings for enhanced output aesthetics.
    - `main()`: The main game loop coordinating gameplay.

- **`test_project.py`:**
  - Contains unit tests for key functions like `makedeck()`, `difficulty()`, and methods from `Dealer` and `Player`.
  - Ensures the correctness of game logic and calculations.

- **`requirements.txt`:**
  - Specifies external dependencies (`colorama`, `tabulate`) required for the project.

#### Design Choices:
1. **Dealer AI:** The difficulty level directly affects the dealer's threshold for standing, making the game more challenging for experienced players.
2. **Card Representation:** Cards are visualized with suit symbols (♥, ♦, ♠, ♣) and formatted neatly for better readability in the terminal.
3. **Reusability:** Core functions like `makedeck()` and `calculate_points()` are modular and can be tested independently.
4. **Error Handling:** The `difficulty()` function handles invalid input gracefully, defaulting to a random difficulty if the input is incorrect.

#### How to Play:
1. Run the `project.py` file.
2. Choose the difficulty level (1: Hard, 2: Medium, 3: Easy).
3. The game begins with both the player and dealer receiving two cards.
4. View your hand and the dealer's visible card.
5. Decide whether to hit (draw another card) or stand (end your turn).
6. Watch as the dealer plays their turn.
7. The winner is determined based on the scores:
   - Closest to 21 without exceeding wins.
   - A tie occurs if both have the same score.
   - A blackjack (21 points) is an instant win.

#### Testing:
The project uses `pytest` for testing:
- Tests ensure the integrity of the deck generation (`makedeck()`).
- Verify the correctness of scoring and hand evaluation.
- Validate dealer and player behaviors under different conditions.

#### Requirements:
To run the project, install the required libraries by running:
```bash
pip install -r requirements.txt
