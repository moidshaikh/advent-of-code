import logging
import os
import re
from collections import defaultdict
from functools import reduce
from typing import Dict, List, Literal, Tuple

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(funcName)s - %(message)s",
    handlers=[logging.FileHandler(f"{__file__}.log"), logging.StreamHandler()],
)

logger = logging.getLogger(__name__)

inputfile: str = os.path.join(
    f"{os.path.dirname(os.path.dirname(__file__))}",
    "inputs",
    f"{os.path.splitext(os.path.basename(__file__))[0]}.in",
)
testing: bool = 0


def read_input() -> str:
    logger.info("Starting to read input data")
    raw_input: str = ""
    if testing:
        logger.debug("Using test input data")
        # here we can input the sample input
        raw_input = """47|53
                        97|13
                        97|61
                        97|47
                        75|29
                        61|13
                        75|53
                        29|13
                        97|29
                        53|29
                        61|53
                        97|53
                        61|29
                        47|13
                        75|47
                        97|75
                        47|61
                        75|61
                        47|29
                        75|13
                        53|13

                        75,47,61,53,29
                        97,61,53,29,13
                        75,29,13
                        75,97,47,61,53
                        61,13,29
                        97,13,75,29,47"""

    else:
        logger.debug(f"Reading from file: {inputfile}")
        try:
            with open(inputfile, "r") as f:
                raw_input = f.read()
        except FileNotFoundError as fnfe:
            logger.critical(f"Error: {fnfe}")  # Show the system error message
            logger.critical(
                "Please create the input file in the format: ./inputs/dec<day: int>.in"
            )
            raise

    # logger.info(f"{raw_input=}")
    return raw_input


def process_input(data: str) -> Dict[str, List]:
    sections = data.strip().split("\n\n")
    page_ordering_rules = []
    pages_to_process = []

    # Parse ordering rules
    for rule in sections[0].splitlines():
        x, y = map(int, rule.split("|"))
        page_ordering_rules.append((x, y))

    # Parse updates
    for update in sections[1].splitlines():
        pages_to_process.append(list(map(int, update.split(","))))

    return {
        "page_ordering_rules": page_ordering_rules,
        "pages_to_process": pages_to_process,
    }


def is_update_in_order(update: List[int], rules: List[Tuple[int, int]]) -> bool:
    # Create a position map for quick lookup
    position = {page: i for i, page in enumerate(update)}
    print(position)

    for x, y in rules:
        # Only check the rules involving pages in the current update
        if x in position and y in position:
            # If x must come before y, but x appears after y, the update is invalid
            if position[x] > position[y]:
                return False
    return True


def solution1(data: str) -> int:
    processed = process_input(data)
    page_ordering_rules = processed["page_ordering_rules"]
    pages_to_process = processed["pages_to_process"]

    total_middle_sum = 0

    for update in pages_to_process:
        if is_update_in_order(update, page_ordering_rules):
            # If the update is valid, find the middle page
            middle_page = update[len(update) // 2]
            total_middle_sum += middle_page

    return total_middle_sum


def solution2(data: str) -> int:
    return 0


def problem1() -> int:
    logger.info("Starting problem 1")
    data: str = read_input()
    result: int = solution1(data)
    return result


def problem2():
    logger.info("Starting problem 2")
    data: str = read_input()
    print(f"{data=}")
    result: int = solution2(data)
    return result


def main(problem_part: Literal[1, 2]):
    res = -1
    try:
        if problem_part not in {1, 2}:
            raise ValueError(f"Invalid argument: {problem_part}. Must be 1 or 2.")

        if problem_part == 1:
            res: int = problem1()
        elif problem_part == 2:
            res: int = problem2()

        logger.info(f"Final result: {res}")
    except ValueError as ve:
        logger.critical(str(ve), exc_info=True)
        raise
    except Exception as e:
        logger.critical(f"An unexpected error occurred: {str(e)}", exc_info=True)
        raise


if __name__ == "__main__":
    logger.info("start")
    main(1)
