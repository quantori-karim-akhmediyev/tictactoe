# Tic Tac Toe

Welcome to Tic Tac Toe! Enjoy this simple, classic game right from your command line. This implementation supports a nxn grid, with a default setting of 3x3. The objective is to align three of your marks in a row, column, or diagonally.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. **Clone the Repository**

   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-repository/tictactoe.git
   cd tictactoe
   ```

2. **Set Up a Virtual Environment**

   Create and activate a virtual environment:

   - **Unix-based systems:**

     ```bash
     python -m venv venv
     source venv/bin/activate
     ```

   - **Windows:**

     ```bash
     python -m venv venv
     .\venv\Scripts\activate
     ```

3. **Install Dependencies**

   Install all the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. **Prepare Your Moves**

   Write your game moves in the `moves.txt` file, formatted as described in the documentation.

2. **Run the Game**

   Execute the game using:

   ```bash
   python main.py moves.txt
   ```

   To view the game board after each move, use the `--show-board` option:

   ```bash
   python main.py --show-board moves.txt
   ```

### Testing

Run automated tests to ensure the game operates correctly:

```bash
python -m unittest discover -s tests
```

### Code Quality

To maintain code quality and style consistency, use the pre-commit hooks:

1. **Install pre-commit hooks:**

   ```bash
   pre-commit install
   ```

2. **Run pre-commit on all files:**

   ```bash
   pre-commit run --all-files
   ```

### Docker Support

If you prefer using Docker:

1. **Build the Docker Image**

   ```bash
   docker build -t tictactoe .
   ```

2. **Run the Docker Container**

   ```bash
   docker run tictactoe
   ```

## Contributing

Contributions are welcome! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.
