

def compute_cost(arr: list) -> int:
    total_burden = 0
    for i, _ in enumerate(arr):
        l = arr[i:] 
        if len(l) == 1: 
            continue
        j = i + l.index(min(l)) + 1
        sub = arr[i:j]
        arr[i:j] = reversed(sub) 
        total_burden += len(sub)
    return total_burden


def main():
    n_cases = int(input())
    for i in range(1, n_cases + 1):
        _ = input()
        elements = [int(x) for x in input().split()]
        result = compute_cost(elements)
        print('Case #{}: {}'.format(i, result))


main()
