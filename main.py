import argparse
import importlib
import os

from common import (
    measure_performance,
    measure_scalability,
    read_input,
    run_tests,
    setup_logging,
)


def load_problem(year, day):
    module = f"solutions.{year}.day{day:02d}"
    return importlib.import_module(module)


def main(year, day, part, test_flag, time_flag, scale_flag):
    setup_logging()

    problem = load_problem(year, day)

    # --- Test mode ---
    if test_flag:
        run_tests(problem)
        return

    # --- Load input + parse ---
    input_path = os.path.join("inputs", str(year), f"day{day:02d}.in")
    raw = read_input(input_path)
    data = problem.parse(raw)

    # choose part
    solution = getattr(problem, f"solution{part}")

    # --- Default run ---
    if not time_flag and not scale_flag:
        print(solution(data))
        return

    # --- Time measurement ---
    if time_flag:
        result, elapsed = measure_performance(solution, data)
        print(f"Result: {result}  (time: {elapsed:.6f}s)")

    # --- Scalability test ---
    if scale_flag:
        if hasattr(problem, "generate_scaled_input"):
            datasets = problem.generate_scaled_input()
        else:
            # fallback: repeat input N times
            base = raw.strip() or "x"
            sizes = [10, 100, 1000, 5000]
            datasets = [(s, problem.parse(base * s)) for s in sizes]

        results = measure_scalability(solution, datasets)
        print("\nSize | Time (s)")
        for s, t in results:
            print(f"{s:5} | {t:.6f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("year", type=int)
    parser.add_argument("day", type=int)
    parser.add_argument("part", type=int, choices=[1, 2])

    parser.add_argument("--test", action="store_true", help="Run built-in tests")
    parser.add_argument("--time", action="store_true", help="Measure runtime")
    parser.add_argument("--scale", action="store_true", help="Run scalability test")

    args = parser.parse_args()
    main(args.year, args.day, args.part, args.test, args.time, args.scale)
