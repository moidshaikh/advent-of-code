import argparse
import logging
import os
from collections import defaultdict
from itertools import combinations
import math

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
testing: bool = True

test_input: str = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""

def read_input() -> str:
    logger.info("Starting to read input data")
    if testing:
        return test_input
    
    logger.debug(f"Reading from file: {inputfile}")
    try:
        with open(inputfile, "r") as f:
            return f.read()
    except FileNotFoundError as fnfe:
        logger.critical(f"Error: {fnfe}")
        logger.critical(
            "Please create the input file in the format: ./inputs/dec<day: int>.in"
        )
        raise

def get_antinodes(p1: tuple[int, int], p2: tuple[int, int], rows: int, cols: int) -> list[tuple[int, int]]:
    """
    Calculate antinodes between two antennas where one is twice as far as the other.
    """
    x1, y1 = p1
    x2, y2 = p2
    
    # Calculate the full vector between points
    dx = x2 - x1
    dy = y2 - y1
    
    # Length of vector
    length = (dx * dx + dy * dy) ** 0.5
    if length == 0:
        return []
        
    # Unit vector components
    ux = dx / length
    uy = dy / length
    
    # We'll extend the line in both directions to get all possible antinodes
    multipliers = [-1, 2]  # One point before first antenna, one after second
    antinodes = []
    
    # Try both directions along the line
    for m in multipliers:
        x_anti = x1 + dx * m
        y_anti = y1 + dy * m
        
        x_rounded = round(x_anti)
        y_rounded = round(y_anti)
        
        if 0 <= x_rounded < rows and 0 <= y_rounded < cols:
            antinodes.append((x_rounded, y_rounded))
    
    return antinodes

def solution1(data: str) -> int:
    grid = [list(row) for row in data.strip().split("\n")]
    rows, cols = len(grid), len(grid[0])
    frequencies = defaultdict(list)
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] != ".":
                frequencies[grid[i][j]].append((i, j))
    logger.debug(f"{frequencies=}")
    antinodes = set()
    for freq, positions in frequencies.items():
        for p1, p2 in combinations(positions, 2):
            logger.debug(f"Processing {freq} pair: {p1} -> {p2}")
            new_antinodes = get_antinodes(p1, p2, rows, cols)
            antinodes.update(new_antinodes)
    logger.info(f"{antinodes=}")
    result_grid = [row[:] for row in grid]
    for x, y in antinodes:
        if result_grid[x][y] == ".":
            result_grid[x][y] = "#"
    for row in result_grid:
        print("".join(row))
    return len(antinodes)




def main(problem_part: int):
    try:
        if problem_part not in {1, 2}:
            raise ValueError(f"Invalid argument: {problem_part}. Must be 1 or 2.")
        
        data = read_input()
        result = solution1(data) if problem_part == 1 else solution2(data)
        logger.info(f"Final result: {result}")
        return result
        
    except Exception as e:
        logger.critical(f"An unexpected error occurred: {str(e)}", exc_info=True)
        raise

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run solution with part 1 or 2.")
    parser.add_argument(
        "--flag",
        type=int,
        choices=[1, 2],
        required=True,
        help="Choose 1 or 2 as the flag.",
    )
    
    args = parser.parse_args()
    main(args.flag)