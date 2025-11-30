import hashlib
import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, project_root)


def parse(raw_data: str) -> str:
    # print(raw_data)
    return raw_data


def solution1(raw_data: str) -> int:
    data: str = parse(raw_data)
    result = -1
    for i in range(9999999):
        s = f"{data}{i}"
        # print(f"\rchecking: {s}", end="")
        res = hashlib.md5(s.encode()).hexdigest()
        if res[:5] == "00000":
            result = i
            break
    # print(f"\n{result=}")
    return result


def solution2(raw_data: str) -> int:
    data: str = parse(raw_data)
    result = -1
    for i in range(9999999):
        s = f"{data}{i}"
        # print(f"\rchecking: {s}", end="")
        res = hashlib.md5(s.encode()).hexdigest()
        if res[:6] == "000000":
            result = i
            break
    # print(f"\n{result=}")
    return result


def run_with_tests():
    # Tests for solution1
    test_cases_solution1 = [
        ("abcdef", 609043),
        ("pqrstuv", 1048970),
    ]

    for i, (input_data, expected) in enumerate(test_cases_solution1):
        result = solution1(input_data)
        assert (
            result == expected
        ), f"Test case {i+1} failed: expected {expected}, got {result}"

    print("All tests for solution1 passed!")

    # Tests for solution2
    test_cases_solution2 = [
        ("abcdef", 6742839),
        ("pqrstuv", 5714438),
    ]

    for i, (input_data, expected) in enumerate(test_cases_solution2):
        result = solution2(input_data)
        assert (
            result == expected
        ), f"Test case {i+1} failed: expected {expected}, got {result}"

    print("All tests for solution2 passed!")


if __name__ == "__main__":
    run_with_tests()
