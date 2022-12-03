from functools import reduce

def part_1():
    # Lowercase item types a through z have priorities 1 through 26.
    # Uppercase item types A through Z have priorities 27 through 52.
    item_scores = {
        **{chr(i + 97): i + 1 for i in range(26)},
        **{chr(i + 65): i + 27 for i in range(26)}
    }
    total_score = 0
    with open('input.txt') as f:
        for line in f.readlines():
            line = line.strip()
            mid_i = len(line) // 2
            comp_1, comp_2  = line[:mid_i], line[mid_i:]
            comp_inter = set(comp_1).intersection(set(comp_2))
            assert len(comp_inter) == 1
            shared_item = comp_inter.pop()
            item_score = item_scores[shared_item] 
            total_score += item_score
    return total_score


def part_2():
    # Lowercase item types a through z have priorities 1 through 26.
    # Uppercase item types A through Z have priorities 27 through 52.
    item_scores = {
        **{chr(i + 97): i + 1 for i in range(26)},
        **{chr(i + 65): i + 27 for i in range(26)}
    }
    total_score = 0
    with open('input.txt') as f:
        rucksacks = []
        for line in f.readlines():
            line = line.strip()
            rucksacks.append(line)
            if len(rucksacks) == 3:
                # process group of three
                comp_inter = reduce(
                    lambda acc, x: acc.intersection(set(x)) if acc else set(x), 
                    rucksacks, 
                    None 
                )
                assert len(comp_inter) == 1
                shared_item = comp_inter.pop()
                item_score = item_scores[shared_item] 
                total_score += item_score
                rucksacks = []
    return total_score


if __name__ == '__main__':
    x = part_2()
    print('x =', x)