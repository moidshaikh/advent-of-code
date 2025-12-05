import logging
import os
import sys

import pytest

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, project_root)
from common import setup_logging

logger = setup_logging(logging.INFO)


def parse(raw_data: str) -> str:
    return raw_data


def solution1(data: str) -> int:
    # data here is cleaned data from parse func above
    return 0


def solution2(data: str) -> int:
    return 0


test_data: str = """1
2
3"""


@pytest.fixture
def input_data() -> str:
    return test_data


@pytest.mark.parametrize(
    "expected, solution",
    [
        (0, solution1),
        (0, solution2),
    ],
)
def test_solutions(input_data, expected, solution):
    result = solution(parse(input_data))
    assert result == expected, f"Expected {expected}, got {result}"
