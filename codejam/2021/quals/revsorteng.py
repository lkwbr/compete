import copy

def compute_possible(n: int, c: int) -> int:
    nums = list(set(range(1, n + 1)))
    batch = list([[num] for num in nums])
    while batch:
        b = batch.pop()
        if len(b) == n:
            # check it 
            burden = compute_burden(b)
            if burden == c:
                return ' '.join([str(x) for x in b])
        else:
            # build onto it
            unused_nums = set(nums) - set(b)
            [batch.append(b + [num]) for num in unused_nums]
    
    return 'IMPOSSIBLE'

    
def compute_burden(arr: list) -> int:
    arr = copy.deepcopy(arr)
    total_burden = 0
    for i, _ in enumerate(arr[:-1]):
        l = arr[i:]
        j = i + l.index(min(l))
        sub = arr[i:j + 1]
        arr[i:j + 1] = reversed(sub)
        burden = j - i + 1
        total_burden += burden
    return total_burden


def main():
    n_cases = int(input())
    for i in range(1, n_cases + 1):
        n, c = [int(x) for x in input().split()]
        result = compute_possible(n, c)
        print('Case #{}: {}'.format(i, result))


#xyz huh? [1, 2, 3, 4] 6 6 True
#print(compute_burden([1, 2, 3, 4]))
#print(compute_burden([4, 2, 1, 3]))
#print(compute_burden([4, 3, 2, 1]))

#print(compute_burden([4, 2, 1, 3]))
#print(compute_burden(list(reversed([7, 6, 5, 4, 3, 2, 1]))))
main()
