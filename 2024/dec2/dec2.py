# TASK1
# input: 2X2 grid
# each line represents reports
# check if reports are safe
# report is safe if:
#           1. The levels are either all increasing or all decreasing.
#           2. Any two adjacent levels differ by at least one and at most three.
# RETURN: How many reports are safe?
# Approach:
# read in lines,
# for each line, check if report is safe or not, if safe, add it to total and return safelines

# TASK2: Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.


from typing import List

inputfile: str = "../inputs/day2in"
testing: bool = 0


def read_input() -> List[List[int]]:
    if testing:
        raw_input = """7 6 4 2 1
                        1 2 7 8 9
                        9 7 6 2 1
                        1 3 2 4 5
                        8 6 4 4 1
                        1 3 6 7 9"""
    else:
        with open(inputfile, "r") as f:
            raw_input = f.read()
    lines = raw_input.split("\n")
    lines = [list(map(int, x.split())) for x in lines]
    return lines


def reportcheck1(lst: List[int]) -> bool:
    # we check if list is all increasing or all decreasing
    if len(lst) < 2:  # A single element or empty list return true
        return True
    # all increasing
    increasing: bool = all(lst[i] < lst[i + 1] for i in range(len(lst) - 1))
    decreasing: bool = all(lst[i] > lst[i + 1] for i in range(len(lst) - 1))
    return increasing or decreasing


def reportcheck2(lst: List[int]) -> bool:
    # here we check if Any two adjacent levels differ by at least one and at most three.
    if len(lst) < 2:
        return False
    # Check if all adjacent differences satisfy 1 ≤ |difference| ≤ 3
    return all(1 <= abs(lst[i] - lst[i + 1]) <= 3 for i in range(len(lst) - 1))


def problem1():
    data: List[List[int]] = read_input()
    # print(data)
    safe_reports: int = 0
    for report in data:
        if reportcheck1(report) and reportcheck2(report):
            safe_reports += 1
    return safe_reports


def main():
    res: int = problem1()
    print(res)


main()
