import logging
import os
import importlib
import sys

from common import setup_logging, read_input

def main(year: int, problem_number: int, problem_part: int):
    # Set up logging
    setup_logging()

    # Load the appropriate solution module based on the year and problem number
    problem_module = importlib.import_module(f"solutions.{year}.dec{problem_number:02d}")

    # Prepare the input file path
    inputfile = os.path.join("inputs", str(year), f"dec{problem_number:02d}.in")
    data = read_input(inputfile)

    # Execute the appropriate solution based on the problem part
    if problem_part == 1:
        result = problem_module.solution1(data)
    elif problem_part == 2:
        result = problem_module.solution2(data)
    
    logging.info(f"Result for {year}, problem {problem_number}, part {problem_part}: {result}")

if __name__ == "__main__":
    if len(sys.argv) != 4 or not sys.argv[1].isdigit() or not sys.argv[2].isdigit() or sys.argv[3] not in {'1', '2'}:
        logging.critical("Usage: python main.py <year> <problem_number> <problem_part>")
        sys.exit(1)
    
    year = int(sys.argv[1])
    problem_number = int(sys.argv[2])
    problem_part = int(sys.argv[3])
    main(year, problem_number, problem_part)
