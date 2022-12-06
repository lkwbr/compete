from functools import reduce
import re


def part_1():
    with open('input.txt') as f:
        line = f.readlines()[0].strip()
    window_len = 4
    for i in range(len(line) - window_len):
        window = line[i:i+window_len] 
        if window_len == len(set(window)):
            return i + window_len


def part_2():
    with open('input.txt') as f:
        line = f.readlines()[0].strip()
    window_len = 14
    for i in range(len(line) - window_len):
        window = line[i:i+window_len] 
        if window_len == len(set(window)):
            return i + window_len


if __name__ == '__main__':
    x = part_2()
    print('x =', x)