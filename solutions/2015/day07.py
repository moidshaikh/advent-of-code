import os
import sys

from common import setup_logging

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, project_root)
logger = setup_logging()


def parse(raw_data: str) -> list[str]:
    # Split the raw input into lines and filter out empty lines
    return [line for line in raw_data.strip().split("\n") if line]


def parse_instructions(instructions: list[str]) -> dict[str, str]:
    wires = {}
    for line in instructions:
        # Split at " -> "
        parts = line.strip().split(" -> ")
        if len(parts) != 2:
            logger.warning(f"Skipping invalid instruction: {line}")
            continue
        operation = parts[0].strip()  # Operation before arrow
        output = parts[1].strip()  # Output after arrow

        # Map the operation to the output
        wires[output] = operation

    return {key: val for key, val in sorted(wires.items())}


def solution1(data):
    logger.info(f"{type(data)}: {data[1]}")
    instructions = parse_instructions(data)

    gates: dict[str, int] = {}
    sk = sorted(instructions, key=lambda k: len(instructions[k]), reverse=False)

    while True:
        any_updated = False

        for k in sk:
            if k in gates:
                logger.info(f"{k} found in gates, skipping.")
                continue

            v = instructions[k]

            # Handle direct numeric assignments
            if len(v) == 1 and v[0].isnumeric():
                gates[k] = int(v[0])
                any_updated = True

            # Handle NOT operations
            elif len(v) == 2 and "NOT" in v:
                op = v[-1]
                if op.isalpha() and op in gates:
                    gates[k] = ~gates[op] & 65535
                    any_updated = True

            # Handle binary operations
            elif len(v) == 3:
                op1, op2 = v[0], v[-1]
                op1_value = (
                    gates[op1]
                    if op1.isalpha() and op1 in gates
                    else int(op1) if op1.isnumeric() else None
                )
                op2_value = (
                    gates[op2]
                    if op2.isalpha() and op2 in gates
                    else int(op2) if op2.isnumeric() else None
                )

                if "AND" in v and op1_value is not None and op2_value is not None:
                    gates[k] = op1_value & op2_value
                    any_updated = True
                elif "OR" in v and op1_value is not None and op2_value is not None:
                    gates[k] = op1_value | op2_value
                    any_updated = True
                elif "LSHIFT" in v and op1_value is not None:
                    gates[k] = op1_value << op2_value
                    any_updated = True
                elif "RSHIFT" in v and op1_value is not None:
                    gates[k] = op1_value >> op2_value
                    any_updated = True

            # Log if no operator was found
            else:
                logger.info(f"No Operator found: {v}")

        # Break the loop if no gates were updated
        if not any_updated:
            break

    logger.info(gates)
    return gates["a"]


def solution2(data: str) -> int:
    return 0


def test_solutions():
    # Tests for solution1
    test_cases_solution1 = [
        (
            """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i""",
            0,
        ),
    ]

    for i, (input_data, expected) in enumerate(test_cases_solution1):
        result = solution1(input_data)
        assert (
            result == expected
        ), f"Test case {i+1} failed: expected {expected}, got {result}"

    logger.info("All tests for solution1 passed!")

    # Tests for solution2
    test_cases_solution2 = [
        ("", 0),
    ]

    for i, (input_data, expected) in enumerate(test_cases_solution2):
        result = solution2(input_data)
        assert (
            result == expected
        ), f"Test case {i+1} failed: expected {expected}, got {result}"

    logger.info("All tests for solution2 passed!")
