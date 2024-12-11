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


def parse_input(input_text: str) -> Tuple[Dict[int, Set[int]], List[List[int]]]:
    """
    Parse the input text into rules and updates.
    Returns tuple of (rules_dict, updates_list).
    """
    rules_dict = defaultdict(set)
    updates = []

    lines = input_text.strip().split("\n")
    rules_section = True

    for line in lines:
        if not line:
            rules_section = False
            continue

        if rules_section:
            before, after = map(int, line.split("|"))
            rules_dict[before].add(after)
        else:
            update = list(map(int, line.split(",")))
            updates.append(update)

    return dict(rules_dict), updates


def build_graph(numbers: List[int], rules: Dict[int, Set[int]]) -> Dict[int, Set[int]]:
    """
    Build adjacency graph for the given numbers using only applicable rules.
    """
    numbers_set = set(numbers)
    graph = defaultdict(set)

    for num in numbers:
        if num in rules:
            # Only include edges where both numbers are in the update
            graph[num].update(after for after in rules[num] if after in numbers_set)

    return dict(graph)


def topological_sort(graph: Dict[int, Set[int]], numbers: Set[int]) -> List[int]:
    """
    Perform topological sort on the graph.
    Returns ordered list of numbers.
    """
    # Calculate in-degrees
    in_degree = {num: 0 for num in numbers}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    # Initialize queue with nodes having no dependencies
    queue = deque([num for num in numbers if in_degree[num] == 0])
    result = []

    while queue:
        current = queue.popleft()
        result.append(current)

        if current in graph:
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

    return result if len(result) == len(numbers) else []


def is_valid_order(numbers: List[int], rules: Dict[int, Set[int]]) -> bool:
    """
    Check if the given order is valid according to the rules.
    """
    positions = {num: i for i, num in enumerate(numbers)}

    for num in numbers:
        if num in rules:
            for after in rules[num]:
                if after in positions and positions[num] > positions[after]:
                    return False
    return True


def get_correct_order(update: List[int], rules: Dict[int, Set[int]]) -> List[int]:
    """
    Get the correct order for an update using topological sort.
    """
    graph = build_graph(update, rules)
    return topological_sort(graph, set(update))


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


def solution2(input_text: str) -> int:
    """
    Solve part 2 of the puzzle:
    1. Parse input to get rules and updates
    2. Identify incorrectly ordered updates
    3. Sort them according to rules
    4. Find middle numbers and sum them

    Args:
        input_text (str): Raw puzzle input containing rules and updates

    Returns:
        int: Sum of middle numbers from correctly ordered invalid updates
    """
    rules, updates = parse_input(input_text)

    # Find invalid updates and their correct orderings
    middle_sum = 0
    for update in updates:
        if not is_valid_order(update, rules):
            correct_order = get_correct_order(update, rules)
            middle_index = len(correct_order) // 2
            middle_sum += correct_order[middle_index]

    return middle_sum


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
    main(2)
