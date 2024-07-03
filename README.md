# Tic Tac Toe

Welcome to Tic Tac Toe! This is a simple command-line based game where two players take turns marking spaces on a nxn grid (3x3 by default). The goal is to get three of your marks in a row, either horizontally, vertically, or diagonally.

## How to Play

1. Clone this repository to your local machine.

2. Open a terminal and navigate to the project directory.

3. Set up a virtual environment by running the command `python -m venv venv`.

4. Activate the virtual environment by running the command `source venv/bin/activate` (for Unix-based systems) or `venv\Scripts\activate` (for Windows).

5. Install the required dependencies by running the command `pip install -r requirements.txt`.

6. Write your commands in the moves.txt file. Write only commands and nothing more.

7. Run the command `python main.py moves.txt` to play the game.

The `python main.py --show-board moves.txt` command plays you the game with printed board.

8. You can run tests with the command `python -m unittest discover -s tests`.

9. To check linters and formatting, you can use pre-commit. Run `pre-commit install` to set it up, and then run `pre-commit run --all-files` to check all files.

