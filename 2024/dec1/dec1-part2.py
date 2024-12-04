# TASK - Day2
# building on day1,
# we need to calculate similarity score
# we calculate similarity_score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.


from collections import Counter

inputfile: str = "./inputs/input"
testing: bool = 0


def read_input() -> tuple[list[int], list[int]]:

    if testing:
        list1 = list(range(20))  # [1,2,3...,19]
        list2 = list(range(0, 20, 2)) + list(
            range(0, 20, 2)
        )  # list with odd numbers twice[0,2...18, 0,2,...18]

        # given input
        list1, list2 = [3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3]

        return list1, list2

    rawdata: str
    with open(inputfile, "r") as f:
        rawdata: str = f.readlines()

    left_list, right_list = [], []
    for line in rawdata:
        l, r = map(int, line.split())
        left_list.append(l)
        right_list.append(r)
    # print(len(left_list), len(right_list))
    return left_list, right_list


def get_similarity_score(list1: list[int], list2: list[int]) -> int:
    # we need to calc how many times num in list1 appears in list2

    ncounter = Counter(list2)  # here we get a dict of {val: times}
    print(f"{len(ncounter)=}")
    # print(f"{len(set(list2))}")
    sim_score = 0
    for n in list1:
        times = ncounter.get(n, 0)
        print(n, times, end="\t\t")
        sim_score += n * times
    print("\n")
    return sim_score


def main():
    left, right = read_input()
    # print(left[-5:], right[-5:])
    # print(left, "\n", right)
    result = get_similarity_score(left, right)
    print(f"result: {result}")


main()
