import copy
import logging
import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, project_root)
from common import setup_logging

logger = setup_logging(level=logging.INFO)
logger.info(f"{project_root=}")


def parse(raw_data: str) -> list[list[str]]:
    logger.info("parse called, ")
    return [list(row) for row in raw_data.split()]


directions = [(i, j) for j in range(-1, 2) for i in range(-1, 2) if (i, j) != (0, 0)]
# directions =  [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]


def fill_roll(total: int, data: list[list[str]]):
    rows = len(data)
    cols = len(data[0])
    # convert previous 'x' removed rolls to '.'
    for r in range(rows):
        for c in range(cols):
            if data[r][c] == "x":
                data[r][c] = "."
    new_data = copy.deepcopy(data)
    for r in range(rows):
        for c in range(cols):
            if data[r][c] != "@":
                continue
            neighbours = 0
            for dx, dy in directions:
                nr, nc = r + dx, c + dy
                if 0 <= nr < rows and 0 <= nc < cols:
                    if data[nr][nc] == "@":
                        neighbours += 1
            if neighbours < 4:
                new_data[r][c] = "x"
                total += 1
    return total, new_data


def solution1(data: list[list[str]]) -> int:
    logger.info(type(data), data)
    r, c = len(data[0]), len(data)
    total: int = 0
    total, data = fill_roll(total, data)
    logger.info(f"{total=}")
    return total


def solution2(data: list[list[str]]) -> int:
    total = 0
    while True:
        before_total = total
        total, data = fill_roll(total, data)
        logger.info(f"{total=}")
        # number removed this iteration
        removed_this_iter = total - before_total
        if removed_this_iter == 0:
            break
    return total


def test_solutions():
    # Tests for solution1
    test_cases_solution1 = [
        (
            "..@@.@@@@.\n@@@.@.@.@@\n@@@@@.@.@@\n@.@@@@..@.\n@@.@@@@.@@\n.@@@@@@@.@\n.@.@.@.@@@\n@.@@@.@@@@\n.@@@@@@@@.\n@.@.@@@.@.",
            13,
        ),
    ]

    for i, (input_data, expected) in enumerate(test_cases_solution1):
        result = solution1(parse(input_data))
        assert (
            result == expected
        ), f"Test case {i+1} failed: expected {expected}, got {result}"

    logger.info("All tests for solution1 passed!")

    # Tests for solution2
    test_cases_solution2 = [
        (
            "..@@.@@@@.\n@@@.@.@.@@\n@@@@@.@.@@\n@.@@@@..@.\n@@.@@@@.@@\n.@@@@@@@.@\n.@.@.@.@@@\n@.@@@.@@@@\n.@@@@@@@@.\n@.@.@@@.@.",
            43,
        ),
    ]

    for i, (input_data, expected) in enumerate(test_cases_solution2):
        result = solution2(parse(input_data))
        assert (
            result == expected
        ), f"Test case {i+1} failed: expected {expected}, got {result}"

    logger.info("All tests for solution2 passed!")
