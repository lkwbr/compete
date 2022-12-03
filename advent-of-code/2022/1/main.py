def part_1():
    most_cals = -1 
    curr_cals = 0
    with open('input.txt') as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                most_cals = max(curr_cals, most_cals)
                curr_cals = 0
            else:
                curr_cals += int(line) 
    return most_cals


def part_2():
    all_cals = []
    curr_cals = 0
    with open('input.txt') as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                all_cals.append(curr_cals)
                curr_cals = 0
            else:
                curr_cals += int(line) 
    top_3_sum = sum(sorted(all_cals)[-3:])
    return top_3_sum


if __name__ == '__main__':
    x = part_2()
    print('x =', x)