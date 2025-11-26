# A opening parenthesis, (, means he should go up one floor,
# a closing parenthesis, ), means he should go down one floor.


def parse(raw_data: str) -> str:
    return raw_data


def solution1(raw_data: str) -> int:
    data: str = parse(raw_data)
    # print("{data=}")
    current = [0, 0]
    houses = [[current[0], current[1]]]
    # {'>': [1,0], '^': [0,1], '<': [-1,0], 'v':[0,-1]}
    for d in data:
        # print(f"checking {d=}")
        if d == ">":
            current[0] += 1
        elif d == "^":
            current[1] += 1
        elif d == "<":
            current[0] -= 1
        elif d == "v":
            current[1] -= 1
        else:
            print("incorrect")
        # print(f"{current=} {houses=}")
        if current not in houses:
            houses.append([current[0], current[1]])
    # print(f"{houses=}")
    return len(houses)


def solution2(raw_data: str) -> int:
    data: str = parse(raw_data)
    # print("{data=}")
    santa = [0, 0]
    robot_santa = [0, 0]
    houses = [[santa[0], santa[1]]]
    # {'>': [1,0], '^': [0,1], '<': [-1,0], 'v':[0,-1]}
    for i, d in enumerate(data):
        if i % 2 == 0:
            if d == ">":
                santa[0] += 1
            elif d == "^":
                santa[1] += 1
            elif d == "<":
                santa[0] -= 1
            elif d == "v":
                santa[1] -= 1
            else:
                print("incorrect")
            if santa not in houses:
                houses.append([santa[0], santa[1]])
        else:
            if d == ">":
                robot_santa[0] += 1
            elif d == "^":
                robot_santa[1] += 1
            elif d == "<":
                robot_santa[0] -= 1
            elif d == "v":
                robot_santa[1] -= 1
            else:
                print("incorrect")
            if robot_santa not in houses:
                houses.append([robot_santa[0], robot_santa[1]])
    # print(f"{houses=}")
    return len(houses)


if __name__ == "__main__":
    # Tests for solution1
    test_cases_solution1 = [
        (">", 2),
        ("^>v<", 4),
        ("^v^v^v^v^v", 2),
    ]

    for i, (input_data, expected) in enumerate(test_cases_solution1):
        result = solution1(input_data)
        assert (
            result == expected
        ), f"Test case {i+1} failed: expected {expected}, got {result}"

    print("All tests for solution1 passed!")

    # Tests for solution2
    test_cases_solution2 = [
        ("^v", 3),
        ("^>v<", 3),
        ("^v^v^v^v^v", 11),
    ]

    for i, (input_data, expected) in enumerate(test_cases_solution2):
        result = solution2(input_data)
        assert (
            result == expected
        ), f"Test case {i+1} failed: expected {expected}, got {result}"

    print("All tests for solution2 passed!")
