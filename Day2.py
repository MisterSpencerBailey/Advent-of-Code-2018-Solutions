# https://adventofcode.com/2018/day/2


def check_sum():
    double_count = 0
    triple_count = 0
    input = open('Day2.txt', 'r').readlines()

    for line in input:
        unique_chars = set(line)
        two_count = False
        three_count = False
        for char in unique_chars:
            if line.count(char) == 2 and two_count is False:
                double_count += 1
                two_count = True
            elif line.count(char) == 3 and three_count is False:
                triple_count += 1
                three_count = True

    return (double_count * triple_count)
