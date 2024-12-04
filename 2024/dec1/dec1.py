# TASK
# input file has 2 cols of numbers
# Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number with the second-smallest right number, and so on. ==>> sort the 2 cols
# Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances. >> find difference between 2 cols.
# SUM the difference and return


# def parser(line):
#     """This will get a line, strip whitespace and return as int"""
#     # print()
#     return list(map(int, line.split()))


def difference_list():
    rawdata: str
    with open("./inputs/input", "r") as f:
        rawdata = f.readlines()

    left_list, right_list = [], []
    for line in rawdata:
        l, r = map(int, line.split())
        left_list.append(l)
        right_list.append(r)

    left_list.sort()
    right_list.sort()
    how_far_apart = 0
    for i in range(len(left_list)):
        how_far_apart += abs(right_list[i] - left_list[i])
        # print(
        #     f"{abs(right_list[i] - left_list[i])=} :: {left_list[i]}, {right_list[i]}"
        # )
    return how_far_apart


def main():
    res = difference_list()
    print(f"result: {res}")


main()
