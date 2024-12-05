# TASK1
# input: string : like: xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
# we have to parse input string and get mul(x,y): mul(2,4) mul(5,5), mul(11,8) mul(8,5)
# Next calulate their multiplication and return result: 161 (2*4 + 5*5 + 11*8 + 8*5).
# we can solve it in 2 ways:
# 1. Use regex
# 2. Create own parser


# TASK2: Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.


import logging
import re
from functools import reduce

# Configure logging
logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("december3.log"), logging.StreamHandler()],
)

logger = logging.getLogger(__name__)

inputfile: str = "../inputs/day3.input"
testing: bool = 0


def read_input() -> str:
    logger.info("Starting to read input data")
    if testing:
        logger.debug("Using test input data")
        raw_input = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
    else:
        logger.debug(f"Reading from file: {inputfile}")
        with open(inputfile, "r") as f:
            raw_input = f.read()
    print(raw_input)
    return raw_input


def problem1() -> int:
    logger.info("Starting problem 1")
    data: str = read_input()
    regx = re.compile(r"mul\((\d+)\,(\d+)\)")
    matches = re.findall(regx, data)
    res = 0
    for match in matches:
        res += reduce(lambda x, y: x * y, map(int, match))
    return res


def problem2():
    logger.info("Starting problem 2")
    data: str = read_input()
    logger.debug(f"Input Data: {data}")


def main():
    logger.info("Starting program")
    try:
        res: int = problem1()
        logger.info(f"Final result: {res}")
        print(res)
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}", exc_info=True)
    logger.info("Program completed")


if __name__ == "__main__":
    main()
