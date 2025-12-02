import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, project_root)


def parse(raw_data: str) -> list[str]:
    ranges = raw_data.split(",")
    # print(f"{ranges=}")
    return ranges


def check_invalid1(range_string: str) -> int:
    start, end = map(int, range_string.split("-"))
    invalid = 0
    for i in range(start, end + 1):
        s = str(i)
        half = len(s) // 2
        left, right = str(i)[:half], str(i)[half:]
        if left == right:
            invalid += i
    return invalid


def check_multiple_invalid(num: int) -> bool:
    s = str(num)
    for i in range(1, (len(s) // 2) + 1):
        substr = s[:i]
        multiplier = len(s) // len(s[:i])
        # print(f"Checking {num} :{substr=} {multiplier=} {substr*multiplier}")
        if s == substr * multiplier:
            return True
    return False


def check_invalid2(range_string: list[str]) -> int:
    invalid = 0
    for rangee in range_string:
        start, end = map(int, rangee.split("-"))
        # print(rangee, list(filter(check_multiple_invalid, range(start, end + 1))))
        invalid += sum(list(filter(check_multiple_invalid, range(start, end + 1))))
    return invalid


def solution1(data: list[str]) -> int:
    return sum(map(check_invalid1, data))


def solution2(data: list[str]) -> int:
    return check_invalid2(data)


def test_check_invalids():
    test_cases = {
        "11-22": 33,
        "95-115": 99,
        "998-1012": 1010,
        "1188511880-1188511890": 1188511885,
        "222220-222224": 222222,
        "1698522-1698528": 0,
        "446443-446449": 446446,
        "38593856-38593862": 38593859,
    }

    for test_input, expected in test_cases.items():
        result = check_invalid1(test_input)
        assert (
            result == expected
        ), f"Test case failed: expected {expected}, got {result}"
    print("All test cases for check_invalid function passed.")


def test_solutions():
    # Tests for solution1
    test_cases_solution1 = [
        (
            "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124",
            1227775554,
        ),
    ]

    for i, (input_data, expected) in enumerate(test_cases_solution1):
        result = solution1(parse(input_data))
        assert (
            result == expected
        ), f"Test case {i+1} failed: expected {expected}, got {result}"

    print("All tests for solution1 passed!")

    # Tests for solution2
    test_cases_solution2 = [
        (
            "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124",
            4174379265,
        ),
    ]

    for i, (input_data, expected) in enumerate(test_cases_solution2):
        result = solution2(parse(input_data))
        assert (
            result == expected
        ), f"Test case {i+1} failed: expected {expected}, got {result}"

    print("All tests for solution2 passed!")
