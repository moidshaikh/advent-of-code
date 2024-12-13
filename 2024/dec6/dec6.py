import logging
import os
import re
from collections import defaultdict, deque
from functools import reduce
from typing import Dict, List, Literal, Set, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(funcName)s - %(message)s",
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
    raw_input: str = ""
    if testing:
        logger.debug("Using test input data")
        # here we can input the sample input
        raw_input = """....#.....\n.........#\n..........\n..#.......\n.......#..\n..........\n.#..^.....\n........#.\n#.........\n......#..."""

    else:
        logger.debug(f"Reading from file: {inputfile}")
        try:
            with open(inputfile, "r") as f:
                raw_input = f.read()
        except FileNotFoundError as fnfe:
            logger.critical(f"Error: {fnfe}")  # Show the system error message
            logger.critical(
                "Please create the input file in the format: ./inputs/dec<day: int>.in"
            )
            raise

    # logger.info(f"{raw_input=}")
    return raw_input


def solution1(data: str) -> int:
    # Convert input to grid
    grid = [list(line) for line in data.strip().split("\n")]
    rows, cols = len(grid), len(grid[0])

    def get_guard_pos():
        pos = None
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] in "^v<>":
                    pos = (i, j)
                    guard_dir = grid[i][j]
                    break
            if pos:
                break
        return pos, guard_dir

    # Find guard's starting position and direction
    guard_pos, guard_dir = get_guard_pos()

    # Direction mappings
    directions = {
        "^": (-1, 0),  # Up means decreasing row
        "v": (1, 0),  # Down means increasing row
        ">": (0, 1),  # Right means increasing column
        "<": (0, -1),  # Left means decreasing column
    }

    # Right turn mapping
    turn_right = {"^": ">", ">": "v", "v": "<", "<": "^"}

    # Track visited positions
    visited = set()
    x, y = guard_pos
    visited.add((x, y))

    while True:
        # Get movement direction
        dx, dy = directions[guard_dir]
        next_x, next_y = x + dx, y + dy

        # Check if next position is out of bounds
        if not (0 <= next_x < rows and 0 <= next_y < cols):
            break

        # Check if there's an obstacle ahead
        if grid[next_x][next_y] == "#":
            # Turn right
            guard_dir = turn_right[guard_dir]
        else:
            # Move forward
            x, y = next_x, next_y
            visited.add((x, y))
            print(f"{visited=}")

    # Mark visited positions with 'X', preserving obstacles
    for i in range(rows):
        for j in range(cols):
            if (i, j) in visited and grid[i][j] != "#":
                grid[i][j] = "X"

    # Print final grid
    # print("\nFinal grid:")
    # for row in grid:
    #     print("".join(row))

    return len(visited)


def detect_loop(
    grid: List[List[str]], start_pos: Tuple[int, int], start_dir: str
) -> bool:
    rows, cols = len(grid), len(grid[0])

    # Direction mappings
    directions = {"^": (-1, 0), "v": (1, 0), ">": (0, 1), "<": (0, -1)}

    turn_right = {"^": ">", ">": "v", "v": "<", "<": "^"}

    # Track visited positions with directions
    # We need to track direction because same position with different direction means different state
    visited_states = set()
    x, y = start_pos
    current_dir = start_dir

    while True:
        # Current state is position + direction
        current_state = (x, y, current_dir)

        if current_state in visited_states:
            return True  # Found a loop

        visited_states.add(current_state)

        # Get next position
        dx, dy = directions[current_dir]
        next_x, next_y = x + dx, y + dy

        # Check if out of bounds
        if not (0 <= next_x < rows and 0 <= next_y < cols):
            return False

        # Check if there's an obstacle
        if grid[next_x][next_y] == "#" or grid[next_x][next_y] == "O":
            current_dir = turn_right[current_dir]
        else:
            x, y = next_x, next_y


def solution2(input_text: str) -> int:
    # Parse input
    grid = [list(line) for line in input_text.strip().split("\n")]
    rows, cols = len(grid), len(grid[0])

    # Find guard's starting position and direction
    guard_pos = None
    guard_dir = None

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] in "^v<>":
                guard_pos = (i, j)
                guard_dir = grid[i][j]
                grid[i][j] = "."  # Clear guard position for testing
                break
        if guard_pos:
            break

    if not guard_pos:
        raise ValueError("No guard found in the grid!")

    # Try each empty position
    valid_positions = set()

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "." and (i, j) != guard_pos:
                # Try placing obstacle here
                grid[i][j] = "O"

                # Check if this creates a loop
                if detect_loop(grid, guard_pos, guard_dir):
                    valid_positions.add((i, j))

                # Remove the obstacle
                grid[i][j] = "."

    # Optionally visualize one of the solutions
    if valid_positions:
        print("\nExample solution:")
        # Place guard and one obstacle
        test_pos = valid_positions.pop()
        grid[guard_pos[0]][guard_pos[1]] = guard_dir
        grid[test_pos[0]][test_pos[1]] = "O"

        for row in grid:
            print("".join(row))

        # Restore the position to set
        valid_positions.add(test_pos)

    return len(valid_positions)


def problem1() -> int:
    logger.info("Starting problem 1")
    data: str = read_input()
    result: int = solution1(data)
    return result


def problem2():
    logger.info("Starting problem 2")
    data: str = read_input()
    print(f"{data=}")
    result: int = solution2(data)
    print(f"{result=}")
    return result


def main(problem_part: Literal[1, 2]):
    res = -1
    try:
        if problem_part not in {1, 2}:
            raise ValueError(f"Invalid argument: {problem_part}. Must be 1 or 2.")

        if problem_part == 1:
            res: int = problem1()
        elif problem_part == 2:
            res: int = problem2()

        logger.info(f"Final result: {res}")
    except ValueError as ve:
        logger.critical(str(ve), exc_info=True)
        raise
    except Exception as e:
        logger.critical(f"An unexpected error occurred: {str(e)}", exc_info=True)
        raise


if __name__ == "__main__":
    logger.info("start")
    # main(1)
    main(2)
