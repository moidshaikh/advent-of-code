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


def problem2():
    logger.info("Starting problem 2")
    data: str = read_input()
    return 0


def main():
    logger.info("Starting program")
    try:
        res: int = problem1()
        logger.info(f"Final result: {res}")
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)
    logger.info("Program completed")


if __name__ == "__main__":
    logger.info("start")
    main()
