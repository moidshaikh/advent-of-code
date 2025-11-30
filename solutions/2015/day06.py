import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, project_root)


def parse(raw_data: str) -> str:
    return raw_data


def solution1(raw_data: str) -> int: ...


def solution2(raw_data: str) -> int: ...


def run_with_tests():
    # Tests for solution1
    test_cases_solution1 = [
        ("", 0),
    ]

    for i, (input_data, expected) in enumerate(test_cases_solution1):
        result = solution1(input_data)
        assert (
            result == expected
        ), f"Test case {i+1} failed: expected {expected}, got {result}"

    print("All tests for solution1 passed!")

    # Tests for solution2
    test_cases_solution2 = [
        ("", 0),
    ]

    for i, (input_data, expected) in enumerate(test_cases_solution2):
        result = solution2(input_data)
        assert (
            result == expected
        ), f"Test case {i+1} failed: expected {expected}, got {result}"

    print("All tests for solution2 passed!")


if __name__ == "__main__":
    run_with_tests()
