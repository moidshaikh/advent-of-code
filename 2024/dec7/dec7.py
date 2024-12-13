import logging
import os
import re
from collections import defaultdict, deque
from functools import reduce
from typing import Dict, List, Literal, Set, Tuple

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

test_input: str = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""


def read_input() -> str:
    logger.info("Starting to read input data")
    raw_input: str = ""
    if testing:
        raw_input = test_input
        logger.debug("Using test input data")

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


def parse(line: str) -> Dict:
    res, ops = line.split(": ")
    res = int(res)
    operands: List[int] = list(map(int, ops.split(" ")))
    # print(res, operands)
    return [res, operands]


from itertools import product


def solution1(data: str) -> int:
    # Convert input to grid
    lines = [parse(x) for x in data.strip().split("\n")]
    print(lines)  # [{12: [3,4]}, ...]
    operands: List[str] = ["+", "*"]
    calibration_result: int = 0
    for prod, nums in lines:
        ops = list(product(operands, repeat=len(nums) - 1))

        for operator_set in ops:
            res = nums[0]
            for i in range(len(operator_set)):
                if operator_set[i] == "+":
                    res += nums[i + 1]
                if operator_set[i] == "*":
                    res *= nums[i + 1]
            if prod == res:
                calibration_result += res
                print(f"FOUND correct for: {prod}, {nums}\n{calibration_result}")
                break
                # found that values match

    # for

    # evaluate = []
    # for exp in expr:
    #     res=
    #     for op in range(len(exp)):
    #         if op == "+":
    #             ...
    #         elif op == "*":
    #             ...
    #         else:
    #             raise "Invalid operand"
    return calibration_result


def solution2(input_text: str) -> int:
    # Parse input
    return -1


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
    print(f"{result=}")
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
    # main(2)
