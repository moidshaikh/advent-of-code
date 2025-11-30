import logging
import time


def setup_logging():
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )


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
