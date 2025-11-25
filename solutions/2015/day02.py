# Day 02


def parse(raw_data: str) -> list[list[int]]:
    return [list(map(int, x.split("x"))) for x in raw_data.split("\n")]
    # return [[2, 3, 4], [1, 1, 10]]


def solution1(raw_data: str) -> int:
    dimensions: list[list[int]] = parse(raw_data)
    wrapping_paper: int = 0
    for dimension in dimensions:
        # assuming largest is length, smallest is height
        h, w, l = sorted(dimension)
        # area
        area: int = 2 * (l * w + w * h + h * l)
        # slack
        slack: int = h * w
        # print(f"{area=}\t{slack=}")
        wrapping_paper += area + slack
        # print(f"{wrapping_paper=}")
    return wrapping_paper


def solution2(raw_data: str) -> int:
    paper = solution1(raw_data)
    dimensions: list[list[int]] = parse(raw_data)
    ribbon_length: int = 0

    for dimension in dimensions:
        h, w, l = sorted(dimension)
        smallest_perimeter: int = 2 * (h + w)

        volume: int = h * w * l
        ribbon_length += smallest_perimeter + volume
    return ribbon_length
