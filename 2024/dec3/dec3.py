# TASK1
# input: string : like: xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
# we have to parse input string and get mul(x,y): mul(2,4) mul(5,5), mul(11,8) mul(8,5)
# Next calulate their multiplication and return result: 161 (2*4 + 5*5 + 11*8 + 8*5).
# we can solve it in 2 ways:
# 1. Use regex
# 2. Create own parser


# TASK2:
# The do() instruction enables future mul instructions.
# The don't() instruction disables future mul instructions.


import logging
import os
import re
from functools import reduce
from typing import List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler(f"{__file__}.log"), logging.StreamHandler()],
)

logger = logging.getLogger(__name__)

pp = os.path.dirname(os.getcwd())
inputfile: str = os.path.join(
    pp,
    "inputs",
    f"{os.path.splitext(os.path.basename(__file__))[0]}.in",
)
testing: bool = 0


def read_input() -> str:
    logger.info("Starting to read input data")
    if testing:
        logger.debug("Using test input data")
        raw_input = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
        raw_input = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""
        # raw_input = """123456789"""
    else:
        logger.debug(f"Reading from file: {inputfile}")
        with open(inputfile, "r") as f:
            raw_input = f.read()
    # logger.info(f"{raw_input=}")
    return raw_input


def use_regex(data) -> int:
    regx = re.compile(r"mul\((\d+)\,(\d+)\)")
    matches = re.findall(regx, data)
    res = 0
    for match in matches:
        res += reduce(lambda x, y: x * y, map(int, match))
    return res


def parse_data(data, part: int = 1) -> List[str]:
    functions: List[str] = []
    exp_start_flag: bool = False
    expression: str = ""
    open_parenthesis: bool = False
    do_or_dont_flag: bool = True

    i = 0
    while i < len(data):

        # Check if the current slice starts a "mul(" expression
        if data[i : i + 4] == "mul(" and not exp_start_flag:
            exp_start_flag = True
            expression = "mul("
            open_parenthesis = True
            i += 4  # Move past "mul(" to start parsing the arguments
            continue

        # check for do and dont
        if data[i : i + 7] == "don't()":
            if part == 2:
                do_or_dont_flag = False
            i += 7
            continue

        if data[i : i + 4] == "do()":
            if part == 2:
                do_or_dont_flag = True
            i += 4
            continue

        # If within an active expression, collect characters
        if exp_start_flag and open_parenthesis:
            char = data[i]
            # End of a valid expression
            if char == ")":
                expression += char
                if do_or_dont_flag:
                    functions.append(expression)

                # Reset flags and expression for the next match
                exp_start_flag = False
                expression = ""
                open_parenthesis = False
            # Invalid character resets parsing
            elif char not in "0123456789, ":
                exp_start_flag = False
                expression = ""
            # Append valid characters
            else:
                expression += char
        i += 1  # Increment manually
    return functions


def calculate_sum(operands: List[str]):
    final = 0

    for op in operands:
        a, b = op[:-1].split("(")[1].split(",")
        final += int(a) * int(b)

    return final


def problem1() -> int:
    logger.info("Starting problem 1")
    data: str = read_input()
    operands = parse_data(data)
    result = calculate_sum(operands)
    return result


def problem2():
    logger.info("Starting problem 2")
    data: str = read_input()
    operands = parse_data(data, 2)
    result = calculate_sum(operands)
    return result


def main():
    logger.info("Starting program")
    try:
        res: int = problem2()
        logger.info(f"Final result: {res}")
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)
    logger.info("Program completed")


if __name__ == "__main__":
    logger.info("start")
    # main()
    print(__file__)
