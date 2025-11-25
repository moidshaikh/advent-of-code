# A opening parenthesis, (, means he should go up one floor,
# a closing parenthesis, ), means he should go down one floor.


def solution1(raw_data: str) -> int:
    floor: int = 0
    for ch in raw_data:
        if ch == "(":
            floor += 1
        else:
            floor -= 1
    return floor


def solution2(raw_data: str) -> int:
    floor: int = 0
    for i, ch in enumerate(raw_data):
        if ch == "(":
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            return i + 1
