import os
import sys
from itertools import combinations

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, project_root)
from common import setup_logging

logger = setup_logging()


def parse(raw_data: str) -> list[str]:
    return raw_data.split("\n")


def old_find_max(joltage: str, digits=2) -> int:
    s: str = str(joltage)
    max_number: int = -1
    # Generate all combinations of the specified length
    for combo in combinations(s, digits):
        new_number = int("".join(combo))  # Join digits to form a new number
        if new_number > max_number:
            max_number = new_number
    return max_number


def find_max(joltage: str, digits=2) -> int:
    s = joltage.strip()
    n = len(s)
    if digits >= n:
        return int(s)

    removals = n - digits
    stack = []

    for ch in s:
        while stack and removals > 0 and stack[-1] < ch:
            stack.pop()
            removals -= 1
        stack.append(ch)

    # ensure correct length
    result = stack[:digits]
    return int("".join(result))


def solution1(data: list[str]) -> int:
    return sum(list(map(find_max, data)))


def solution2(data: str) -> int:
    if isinstance(data, str):
        banks = parse(data)  # returns list[str]
    else:
        banks = data

    total = 0
    for val in banks:
        jolt = find_max(val, 12)
        total += jolt

    return total


def test_find_max():
    test_cases = [
        ("987654321111111", 98),
        ("811111111111119", 89),
        ("234234234234278", 78),
        ("818181911112111", 92),
    ]
    for inp, expected in test_cases:
        result = find_max(inp)
        assert (
            result == expected
        ), f"Test case failed for {inp}: expected {expected}, got {result}"
    logger.info("All test cases pass for find_max")


def test_find_max_with_digits():
    test_cases = [
        ("987654321111111", 987654321111),
        ("811111111111119", 811111111119),
        ("234234234234278", 434234234278),
        ("818181911112111", 888911112111),
    ]
    for inp, expected in test_cases:
        result = find_max(inp, digits=12)
        assert (
            result == expected
        ), f"Test case failed for {inp}: expected {expected}, got {result}"
    logger.info("All test cases pass for find_max")


def test_solutions():
    # Tests for solution1
    test_cases_solution1 = [
        (
            """987654321111111\n811111111111119\n234234234234278\n818181911112111""",
            357,
        ),
    ]

    for i, (input_data, expected) in enumerate(test_cases_solution1):
        result = solution1(parse(input_data))
        assert (
            result == expected
        ), f"Test case {i+1} failed for {input_data}:: expected {expected}, got {result}"

    print("All tests for solution1 passed!")

    # Tests for solution2
    test_cases_solution2 = [
        (
            "987654321111111\n811111111111119\n234234234234278\n818181911112111",
            3121910778619,
        ),
    ]

    for i, (input_data, expected) in enumerate(test_cases_solution2):
        result = solution2(input_data)
        assert (
            result == expected
        ), f"Test case {i+1} failed for {input_data}: expected {expected}, got {result}"

    print("All tests for solution2 passed!")
