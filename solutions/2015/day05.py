import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, project_root)


def parse(raw_data: str) -> list[str]:
    return raw_data.split("\n")


def is_nice_string(s: str) -> bool:
    # 3: It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
    vowels: list[str] = ["a", "e", "i", "o", "u"]
    forbidden: set[str] = {"ab", "cd", "pq", "xy"}
    if any(x in s for x in forbidden):
        return False

    # 1: It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    # 2: It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
    vowel_count: int = 1 if s[0] in vowels else 0
    twice_letter: bool = False

    for i in range(1, len(s)):
        c: str = s[i]
        if c in vowels:
            vowel_count += 1
        if c == s[i - 1]:
            twice_letter = True

    return True if all([vowel_count >= 3, twice_letter]) else False


def is_nice_string2(s: str) -> bool:
    # Check for a pair of letters that appears twice without overlapping
    has_double_pair = any(s.count(s[i : i + 2]) >= 2 for i in range(len(s) - 1))

    # Check for a letter that repeats with exactly one letter between
    has_repeat_with_one_between = any(s[i] == s[i + 2] for i in range(len(s) - 2))

    # A string is nice if both conditions are true
    return has_double_pair and has_repeat_with_one_between


def solution1(data: list[str]) -> int:
    return sum(list(map(is_nice_string, data)))


def solution2(data: str) -> int:
    return sum(list(map(is_nice_string2, data)))


def test_is_nice_string2():
    # Test cases directly from the problem description
    test_cases = [
        # Nice strings
        ("qjhvhtzxzqqjkmpb", True, "has pair (qj) and repeat with one between (zxz)"),
        ("xxyxx", True, "has pair and repeat with overlap"),
        # Naughty strings
        ("uurcxstgmygtbstg", False, "has pair (tg) but no repeat with one between"),
        ("ieodomkazucvgmuy", False, "has repeat with one between (odo) but no pair"),
    ]

    # Run tests
    for s, expected, description in test_cases:
        result = is_nice_string2(s)
        assert (
            result == expected
        ), f"{s}: {description} - Expected {expected}, got {result}"
        print(f"{s}: {'Nice' if result else 'Naughty'} ✓ ({description})")

    print("\nAll test cases passed!")


def test_solution():
    # Tests for solution1
    test_cases_solution1 = [
        (["ugknbfddgicrmopn"], 1),
        (["aaa"], 1),
        (["jchzalrnumimnmhp"], 0),
        (["haegwjzuvuyypxyu"], 0),
        (["dvszwmarrgswjxmb"], 0),
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
