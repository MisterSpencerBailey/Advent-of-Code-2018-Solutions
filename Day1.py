# https://adventofcode.com/2018/day/1


def find_frequency():
    frequency = 0
    file = open("Day1.txt", "r").readlines()
    for value in file:
        frequency += int(value)
    return frequency
