# TASK1
# input: string array
# find XMAS word either horizontal, vertical, diagonal, written backwards, or even overlapping other words.

# TASK2:


import logging
import os
import re
from functools import reduce
from typing import List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(f"{__file__}.log"), logging.StreamHandler()],
)

logger = logging.getLogger(__name__)

inputfile: str = os.path.join(
    f"{os.path.dirname(os.path.dirname(__file__))}",
    "inputs",
    f"{os.path.splitext(os.path.basename(__file__))[0]}.in",
)
testing: bool = 0


def read_input() -> str:
    logger.info("Starting to read input data")
    if testing:
        logger.debug("Using test input data")
        raw_input = """MMMSXXMASM
                        MSAMXMSMSA
                        AMXSXMAAMM
                        MSAMASMSMX
                        XMASAMXAMM
                        XXAMMXXAMA
                        SMSMSASXSS
                        SAXAMASAAA
                        MAMMMXMMMM
                        MXMXAXMASX"""
        # raw_input = """bat\nabt\ntab"""
    else:
        logger.debug(f"Reading from file: {inputfile}")
        with open(inputfile, "r") as f:
            raw_input = f.read()
    # logger.info(f"{raw_input=}")
    return raw_input


def find_xmas(data: str) -> int:
    # SOLUTION 1: Brute Force
    # Convert the input into a grid
    data_grid = [list(line.strip()) for line in data.split("\n")]
    rows, cols = len(data_grid), len(data_grid[0])

    # Create a blank grid to store the solution
    solution_grid = [["." for _ in range(cols)] for _ in range(rows)]

    # Define all possible directions (dx, dy)
    directions = [
        (-1, 0),  # Up
        (-1, -1),  # Up-left
        (-1, 1),  # Up-right
        (1, -1),  # Down-left
        (0, 1),  # Right
        (1, 0),  # Down
        (0, -1),  # Left
        (1, 1),  # Down-right
    ]

    target = "XMAS"
    target_length = len(target)

    def is_valid_position(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def search_and_mark(x, y):
        # Check if the current character matches the first character of "XMAS"
        if data_grid[x][y] != target[0]:
            return 0

        occurrences = 0
        # Explore all 8 directions
        for dx, dy in directions:
            found = True
            temp_positions = []  # To store positions of the current match
            for k in range(target_length):
                nx, ny = x + dx * k, y + dy * k
                if not is_valid_position(nx, ny) or data_grid[nx][ny] != target[k]:
                    found = False
                    break
                temp_positions.append((nx, ny))

            # Mark the positions if a match is found
            if found:
                occurrences += 1
                for px, py in temp_positions:
                    solution_grid[px][py] = data_grid[px][py]
        return occurrences

    # Count total occurrences and update the solution grid
    total_count = 0
    for i in range(rows):
        for j in range(cols):
            total_count += search_and_mark(i, j)

    # Convert the solution grid back to a string format
    highlighted_solution = "\n".join("".join(row) for row in solution_grid)
    # logger.info(f"SOLUTION : \n\n{highlighted_solution}\n")

    return total_count


def problem1() -> int:
    logger.info("Starting problem 1")
    data: str = read_input()
    result: int = find_xmas(data)
    return result


def find_xmas_part2(data: str) -> int:
    """
    Find and count X-shaped patterns in a grid where each diagonal spells 'MAS' or 'SAM'.
    The function looks for X patterns where:
    - The center must be 'A'
    - Each diagonal must spell either 'MAS' or 'SAM' (forwards or backwards)
    - The X pattern shares a central 'A'

    Example valid pattern:
        M.S
        .A.
        M.S

    Args:
        data (str): Input grid as a multi-line string where each line represents a row
                   and each character represents a position in the grid

    Returns:
        int: Number of valid X-MAS patterns found in the grid

    Time Complexity: O(RC) where R is number of rows and C is number of columns
    Space Complexity: O(RC) for storing input and solution grids

    Note:
        The function also prints a solution grid showing the valid X-MAS patterns found,
        with non-pattern positions marked as '.'
    """
    # Convert the input into a grid
    grid = [list(line.strip()) for line in data.split("\n")]
    rows, cols = len(grid), len(grid[0])

    # Create solution grid
    solution = [["." for _ in range(cols)] for _ in range(rows)]

    def is_valid_mas(a, b, c):
        return (a + b + c == "MAS") or (a + b + c == "SAM")

    def check_pattern(r, c):
        # Check bounds first
        if not (0 < r < rows - 1 and 0 < c < cols - 1):
            return False

        # Center must be 'A'
        if grid[r][c] != "A":
            return False

        # Check both diagonals
        diagonal1 = grid[r - 1][c - 1] + grid[r][c] + grid[r + 1][c + 1]
        diagonal2 = grid[r - 1][c + 1] + grid[r][c] + grid[r + 1][c - 1]

        # If valid, mark solution grid
        if is_valid_mas(*diagonal1) and is_valid_mas(*diagonal2):
            solution[r][c] = grid[r][c]  # Center A
            solution[r - 1][c - 1] = grid[r - 1][c - 1]  # Top-left
            solution[r - 1][c + 1] = grid[r - 1][c + 1]  # Top-right
            solution[r + 1][c - 1] = grid[r + 1][c - 1]  # Bottom-left
            solution[r + 1][c + 1] = grid[r + 1][c + 1]  # Bottom-right
            return True

        return False

    # Count valid patterns
    count = sum(
        check_pattern(r, c) for r in range(1, rows - 1) for c in range(1, cols - 1)
    )

    if testing:  # Print solution grid
        print("SOLUTION:\n")
        print("\n".join("".join(row) for row in solution))
        print()

    return count


def problem2():
    logger.info("Starting problem 2")
    data: str = read_input()
    print(f"{data=}")
    result: int = find_xmas_part2(data)
    return result


def main():
    logger.info("Starting program")
    try:
        res: int = problem2()
        logger.info(f"Final result: {res}")
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)
    logger.info("Program completed")


if __name__ == "__main__":
    logger.info("start")
    main()
