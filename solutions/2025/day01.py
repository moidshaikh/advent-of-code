import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, project_root)


def parse(raw_data: str) -> list[int]:
    """We have inputs as `L23` or `R12` separated by `\n`
    We convert it to list of integers with `-` if L and `+` if R.
    """
    data: list[str] = raw_data.split("\n")
    # if L move left, if R move right. we can consider positive and negative steps
    steps: list[int] = []
    for stp in data:
        d, n = stp[0], int(stp[1:])
        if d == "L":
            n *= -1
        steps.append(n)
    return steps


def solution1(data: list[int]) -> int:
    # print(f"Steps after parsing: {data=}")
    li: list[int] = list(range(100))

    def rotate(current: int, steps: int) -> int:
        return (current + steps) % len(li)

    curr: int = 50
    password: int = 0
    for step in data:
        curr = rotate(curr, step)
        # print(f"{curr}", end=" ")
        if curr == 0:
            password += 1
    return password


def solution2(data: list[int]) -> int:
    """
    Count how many times the pointer lands on index 0 while moving one step at a
    time. The list length is 100 and the pointer starts at index 50.
    """
    list_len = 100
    curr = 50  # start position
    password = 0

    for step in data:
        # direction: +1 for right, –1 for left
        sign = 1 if step > 0 else -1

        # walk one unit at a time, counting each landing on 0
        for _ in range(abs(step)):
            curr = (curr + sign) % list_len
            if curr == 0:
                password += 1

    return password


def test_solutions():
    # Tests for solution1
    test_cases_solution1 = [
        (
            """L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82""",
            3,
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
            """L68\nL30\nR48\nL5\nR60\nL55\nL1\nL99\nR14\nL82""",
            6,
        ),
        # Simple single rotation to zero
        (
            """R50""",
            1,
        ),
        # Multiple full rotations
        (
            """R100\nL100""",
            2,
        ),
        # Mixed rotations with multiple zero crossings
        (
            """L25\nR75\nL50""",
            1,
        ),
        # Large rotations
        (
            """R1000""",
            10,
        ),
    ]

    for i, (input_data, expected) in enumerate(test_cases_solution2):
        result = solution2(parse(input_data))
        assert (
            result == expected
        ), f"Test case {i+1} failed: expected {expected}, got {result}"

    print("All tests for solution2 passed!")
