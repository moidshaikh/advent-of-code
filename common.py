import logging
import os
import time
from itertools import chain
from typing import Any, Callable, List, Tuple


def setup_logging(level: int = logging.INFO) -> logging.Logger:
    os.makedirs("logs", exist_ok=True)
    logger = logging.getLogger("common_logger")
    logger.setLevel(level)

    ch = logging.StreamHandler()
    ch.setLevel(level)

    fh = logging.FileHandler("logs/application.log")
    fh.setLevel(level)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - "
        "File: %(filename)s - Function: %(funcName)s - Line: %(lineno)d - "
        "Message: %(message)s"
    )

    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger


def read_input(path: str) -> str:
    """Reads content from a specified file."""
    with open(path, "r") as f:
        return f.read()


def run_tests(problem: Any) -> None:
    """Runs tests defined in the problem object and asserts expected outcomes."""
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


def measure_performance(fn: Callable[[Any], Any], data: Any) -> Tuple[Any, float]:
    """Measures the execution time of a function."""
    start = time.perf_counter()
    result = fn(data)
    return result, time.perf_counter() - start


def measure_scalability(
    fn: Callable[[Any], Any], datasets: List[Tuple[int, Any]]
) -> List[Tuple[int, float]]:
    """Measures the scalability of a function using given datasets."""
    out = []
    for size, data in datasets:
        _, t = measure_performance(fn, data)
        out.append((size, t))
    return out


def flatten(nested_list: List[List[Any]]) -> List[Any]:
    """
    Flatten a nested list of lists into a single list.

    Parameters:
    nested_list (List[List[Any]]): A list containing sublists to be flattened.

    Returns:
    List[Any]: A flat list containing all elements from the nested list.

    Raises:
    TypeError: If the input is not a list of lists.
    """

    if not isinstance(nested_list, list) or any(
        not isinstance(sublist, list) for sublist in nested_list
    ):
        raise TypeError("Input must be a list of lists.")

    return list(chain.from_iterable(nested_list))
