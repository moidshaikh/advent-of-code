import logging
import os
import time


def setup_logging():
    # Create logs directory if it doesn't exist
    os.makedirs("logs", exist_ok=True)
    # Create a logger
    logger = logging.getLogger("common_logger")
    logger.setLevel(logging.INFO)
    # Create console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    # Create file handler
    fh = logging.FileHandler("logs/application.log")
    fh.setLevel(logging.INFO)
    # Create a formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - "
        "File: %(filename)s - Function: %(funcName)s - Line: %(lineno)d - "
        "Message: %(message)s"
    )
    # Add formatter to handlers
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)
    # Add the handlers to the logger
    logger.addHandler(ch)
    logger.addHandler(fh)
    return logger


def read_input(path):
    with open(path) as f:
        return f.read()


def run_tests(problem):
    if not hasattr(problem, "tests"):
        print("No tests defined.")
        return

    for i, (raw, exp1, exp2) in enumerate(problem.tests, 1):
        data = problem.parse(raw)

        if exp1 is not None:
            assert problem.solution1(data) == exp1, f"Test {i} part1 failed"

        if exp2 is not None:
            assert problem.solution2(data) == exp2, f"Test {i} part2 failed"

    print("All tests passed!")


def measure_performance(fn, data):
    start = time.perf_counter()
    result = fn(data)
    return result, time.perf_counter() - start


def measure_scalability(fn, datasets):
    out = []
    for size, data in datasets:
        _, t = measure_performance(fn, data)
        out.append((size, t))
    return out
