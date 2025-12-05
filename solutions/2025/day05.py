import logging
import os
import sys

import pytest

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, project_root)
from common import flatten, setup_logging

logger = setup_logging(logging.INFO)


def parse(raw_data: str) -> tuple[list[str], list[int]]:
    raw2 = raw_data.split("\n\n")
    ranges: list[str] = raw2[0].split("\n")
    ingredients: list[int] = list(map(int, raw2[1].split("\n")))
    # print(f"{ranges}")
    # print(f"{ingredients}")
    return ranges, ingredients


def solution1(data: tuple[list[str], list[int]]) -> int:
    ranges, numbers = data
    # Convert ranges to a list of tuples and sort them
    sorted_ranges = sorted(
        (int(low), int(high)) for low, high in (rang.split("-") for rang in ranges)
    )
    print(f"{sorted_ranges=}")
    fresh: list[int] = []
    for num in numbers:
        # Check if the number is in any of the ranges
        for low, high in sorted_ranges:
            if low <= num <= high:
                fresh.append(num)
                break
    print(f"{fresh=}")
    return len(fresh)


def solution2(data: tuple[list[str], list[int]]) -> int:
    ranges, numbers = data
    sorted_ranges = sorted(
        (int(low), int(high)) for low, high in (rang.split("-") for rang in ranges)
    )
    # print(f"{sorted_ranges=}")
    # we get. sorted_ranges=[(3, 5), (10, 14), (12, 18), (16, 20)]. now we need to merge the ranges.

    total_fresh_ids = 0
    prev_start, prev_end = sorted_ranges[0]

    for curr_start, curr_end in sorted_ranges[1:]:
        if curr_start <= prev_end:  # Overlapping ranges
            prev_end = max(prev_end, curr_end)  # Merge ranges
        else:
            total_fresh_ids += (
                prev_end - prev_start + 1
            )  # Count fresh IDs for the previous range
            prev_start, prev_end = curr_start, curr_end  # Move to the next range

    # Add the last merged range
    total_fresh_ids += prev_end - prev_start + 1

    return total_fresh_ids


test_data: str = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


@pytest.fixture
def input_data() -> str:
    return test_data


@pytest.mark.parametrize(
    "expected, solution",
    [
        (3, solution1),
        (14, solution2),
    ],
)
def test_solutions(input_data, expected, solution):
    result = solution(parse(input_data))
    assert result == expected, f"Expected {expected}, got {result}"
