
def minimize(x: int, y: int, data: list) -> int:
    # x => CJ 
    # y => JC
    # min the cost

    def rev(data):
        last_d = data[0]
        new_data = [last_d]
        for d in data[1:]: 
            if d == '?':
                d = last_d
            last_d = d
            new_data.append(d)
        return new_data

    # forward pass
    data = rev(data)
    # backpass
    data = list(reversed(rev(list(reversed(data)))))

    data = ''.join(data)
    x_cost = data.count('CJ') * x
    y_cost = data.count('JC') * y

    return x_cost + y_cost

    
def main():
    n_cases = int(input())
    for i in range(1, n_cases + 1):
        x, y, data = input().split()
        x = int(x); y = int(y)   
        result = minimize(x, y, data)
        print('Case #{}: {}'.format(i, result))


main()
