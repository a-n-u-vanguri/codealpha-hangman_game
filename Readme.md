# 🎉 Hangman Game 🎉

Welcome to the Hangman game! This is a simple text-based game where you can guess letters to uncover a hidden word based on different categories. The game will provide hints and display a hangman figure based on your incorrect guesses.

## 📚 Table of Contents

- [Game Overview](#game-overview)
- [Categories](#categories)
- [How to Play](#how-to-play)
- [Game Functions](#game-functions)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [License](#license)

## 🕹️ Game Overview

In this Hangman game, players will choose a category and then try to guess the letters of a word related to that category. For every incorrect guess, a part of the hangman figure will be drawn. The goal is to guess the word before the hangman is fully drawn. 

## 🌍 Categories

The game includes the following categories:

1. **Science** 🔬
   - Examples: atom, biology, chemistry, physics, quantum, molecule, enzyme, gravity

2. **Movies** 🎬
   - Examples: inception, avatar, godfather, jaws, matrix, joker, gladiator, titanic

3. **Cities** 🌆
   - Examples: newyork, tokyo, paris, london, mumbai, sydney, moscow, dubai

4. **Famous Landmarks** 🗽
   - Examples: eiffel, pyramids, colosseum, greatwall, tajmahal, machupicchu, statueofliberty, christredeemer

5. **Music** 🎶
   - Examples: beatles, mozart, beethoven, elvis, bach, madonna, nirvana, adele

6. **Space** 🌌
   - Examples: planet, galaxy, astronaut, blackhole, mars, neptune, telescope, asteroid


## 🎮 How to Play

1. Start the game by choosing a category.
2. A hint will be provided related to the chosen category.
3. Guess letters one at a time to reveal the hidden word.
4. If you guess a letter correctly, it will be displayed in the correct position(s).
5. If you guess incorrectly, a part of the hangman will be drawn.
6. The game ends when you either guess the word or the hangman is fully drawn.

## 🛠️ Game Functions

- `display_man(wrong_guesses)`: Displays the hangman figure based on the number of incorrect guesses.
- `display_hint(hint)`: Displays the current hint with guessed letters and underscores.
- `display_answer(answer)`: Displays the answer with correctly guessed letters.
- `choose_category()`: Allows the player to choose a category from the available options.
- `main()`: The main function that runs the hangman game.

## 🚀 Getting Started

To play the game, simply run the Python script. Make sure you have Python installed on your computer.

```bash
python hangman.py