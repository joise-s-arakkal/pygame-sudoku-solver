# Pygame Sudoku Solver

This is a simple Sudoku solver built using Python and Pygame. The program allows users to visualize the solving process of a 9x9 Sudoku puzzle. You can also interactively solve the puzzle or check if a given puzzle has a solution.

## Features

- Visual representation of the Sudoku board.
- Ability to solve the Sudoku puzzle with a click of a button.
- Highlights solved cells in a different color.
- Displays a message if the puzzle has no solution.

## Requirements

- Python 3.x
- Pygame

## Installation

1. Clone the repository:
   
```bash
git clone https://github.com/joise-s-arakkal/pygame-sudoku-solver.git
cd pygame-sudoku-solver
```

2. Install the required dependencies:
   
```bash
pip install pygame
```

## Usage

1. Run the game:
   
```bash
python3 sudoku_gui_v3.py
```

2. A window will appear with a 9x9 Sudoku grid and a "Solve" button. Clicking the button will attempt to solve the puzzle.

## File Structure
- **sudoku_game.py:** Main file to run the Sudoku game with a GUI using Pygame.
- **sudoku_utils.py:** Contains the utility functions for checking the safety of a number and solving the Sudoku using backtracking.
- **sudoku_config.py:** Holds the board configuration and color settings.

## Screenshots

## How It Works
- The Sudoku board is drawn using Pygame.
- The solve_sudoku() function uses a backtracking algorithm to solve the puzzle.
- When the "Solve" button is pressed, the board gets solved in real-time, updating the display.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
   
