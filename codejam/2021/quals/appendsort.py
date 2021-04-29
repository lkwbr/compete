

def solve(arr: list) -> int:
    total_appends = 0
    a = arr[0]
    for i in range(1, len(arr)):
        b = arr[i]
        if a < b:
            continue
        elif a == b:
        print('a, b', a, b)
    return total_burden


def main():
    n_cases = int(input())
    for i in range(1, n_cases + 1):
        _ = input()
        elements = [int(x) for x in input().split()]
        result = solve(elements)
        print('Case #{}: {}'.format(i, result))


main()
