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


import logging
from collections import Counter
from random import choice
from typing import List

# Configure logging
logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("december2.log"), logging.StreamHandler()],
)

logger = logging.getLogger(__name__)

inputfile: str = "../inputs/day2in"
testing: bool = 0


def read_input() -> List[List[int]]:
    logger.info("Starting to read input data")
    if testing:
        logger.debug("Using test input data")
        raw_input = """7 6 4 2 1
                        1 2 7 8 9
                        9 7 6 2 1
                        1 3 2 4 5
                        8 6 4 4 1
                        1 3 6 7 9"""
    else:
        logger.debug(f"Reading from file: {inputfile}")
        with open(inputfile, "r") as f:
            raw_input = f.read()

    lines = raw_input.split("\n")
    lines = [list(map(int, x.split())) for x in lines]
    logger.debug(f"Parsed input data: {lines}")
    return lines


def problem1():
    logger.info("Starting problem 1")
    data: List[List[int]] = read_input()
    safe_reports = 0
    logger.debug(f"Input Data: {data}")

    for report in data:
        logger.debug(f"Processing Report: {report}")
        if is_safe(report):
            logger.info(f"SAFE: {report}")
            safe_reports += 1
        else:
            logger.info(f"UNSAFE: {report}")

    logger.info(f"Problem 1 result: {safe_reports} safe reports")
    return safe_reports


def problem2():
    logger.info("Starting problem 2")
    data: List[List[int]] = read_input()
    safe_reports = 0
    logger.debug(f"Input Data: {data}")

    for report in data:
        logger.debug(f"Processing Report: {report}")

        # First check if it's safe without any modifications
        if is_safe(report):
            logger.info(f"SAFE without removing any level: {report}")
            safe_reports += 1
            continue

        # If not safe, try removing one number
        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1 :]
            if is_safe(modified_report):
                logger.info(f"SAFE by removing level {i + 1}: {report[i]}")
                safe_reports += 1
                break
        else:
            logger.info(f"UNSAFE: {report}")

    logger.info(f"Problem 2 result: {safe_reports} safe reports")
    return safe_reports


def is_safe(lst: List[int]) -> bool:
    logger.debug(f"Checking safety for sequence: {lst}")

    # Check differences
    for i in range(len(lst) - 1):
        diff = abs(lst[i] - lst[i + 1])
        if not (1 <= diff <= 3):
            logger.debug(f"Invalid difference {diff} between {lst[i]} and {lst[i + 1]}")
            return False

    # Check if sequence is monotonic
    increasing = decreasing = True

    for i in range(len(lst) - 1):
        if lst[i] >= lst[i + 1]:
            increasing = False
        if lst[i] <= lst[i + 1]:
            decreasing = False

    result = increasing or decreasing
    logger.debug(
        f"Sequence {'is' if result else 'is not'} monotonic (increasing={increasing}, decreasing={decreasing})"
    )
    return result


def main():
    logger.info("Starting program")
    try:
        res: int = problem2()
        logger.info(f"Final result: {res}")
        print(res)
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)
    logger.info("Program completed")


if __name__ == "__main__":
    main()
