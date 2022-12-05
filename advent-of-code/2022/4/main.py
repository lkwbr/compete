from functools import reduce

def part_1():
    n_contained = 0
    with open('input.txt') as f:
        for line in f.readlines():
            range_1, range_2 = [
                [int(y) for y in x.split('-')] 
                for x in line.strip().split(',')
            ]
            set_1 = set(range(range_1[0], range_1[1] + 1))
            set_2 = set(range(range_2[0], range_2[1] + 1))
            if set_1.issubset(set_2) or set_2.issubset(set_1):
                # print('Y', range_1, range_2)
                n_contained += 1
            else:
                pass
                # print('N', range_1, range_2)
    return n_contained


def part_2():
    n_overlapped = 0
    with open('input.txt') as f:
        for line in f.readlines():
            range_1, range_2 = [
                [int(y) for y in x.split('-')] 
                for x in line.strip().split(',')
            ]
            set_1 = set(range(range_1[0], range_1[1] + 1))
            set_2 = set(range(range_2[0], range_2[1] + 1))
            over = len(set_1.intersection(set_2))
            if over > 0:
                n_overlapped += 1 
            # print(range_1, range_2, over, n_overlapped)
    return n_overlapped


if __name__ == '__main__':
    x = part_2()
    print('x =', x)