
from functools import reduce
from queue import Queue
import copy


def trysolve(ticks: list, rates: list):

    nticks = [0, 0, 0] # copy.deepcopy(ticks)
    print('trysolve', ticks, rates)
    # Step back the rates in terms of nanoseconds
    nanosecs = 0
    twelve_hours_nanosecs = 12 * 60 * 60 * 10**9 
    # TODO:  If we go back further than 12 hours?
    while nticks != ticks:
        nticks[0] += rates[0]
        nticks[1] += rates[1]
        nticks[2] += rates[2]
        nanosecs += 1
        #print(nanosecs, nticks, ticks)
        if nanosecs >= twelve_hours_nanosecs:
            return None
    result = None
    return result


def permute(l: list) -> list[list]:
    if len(l) == 1:
        return [l]
    ps = []
    for i, x in enumerate(l):
        for y in permute(l[:i] + l[i + 1:]):
            p = [x] + y 
            ps.append(p)
    return ps


def trysolvebetterokay(ticks: list, rates: list) -> list:

    print('bef', ticks, rates)
    assert len(ticks) == len(rates)

    # We precompute our constants; T is the number of ticks it takes for 
    # one revolution (360 degrees) around our clock. 
    T = 60 * 720 * 10**9
    
    # Solve for N, the number of nanoseconds that has passed since the 
    # "zero-out" point at midnight.
    potential_Ns = [ti / (ra % T) for ti, ra in zip(ticks, rates)]
    print('pot', potential_Ns)
    if not all([potential_Ns[0] == pn for pn in potential_Ns]):
        # Ns aren't equal, so this assignment isn't a solution.
        return None
    N = potential_Ns[0]
    print('N', N)
     
    # Knowing N, let's return the time the clock reads for each hand.
    hour = N // 10**9 // 60 // 60
    minute = (N // 10**9 // 60) % 60
    second = (N // 10**9) % 60
    nanosecond = N % 10**9
    return ' '.join([str(x) for x in [hour, minute, second, nanosecond]])


def solve(arr: list) -> int:
    """Some guy has a broken clock and no smartwatch.

    NOTES:
        - 1 tick is equal to 1/12×10^−10 degrees
        - This means that the hours hand rotates exactly 1 tick each nanosecond, 
          the minutes hand rotates exactly 12 ticks each nanosecond 
          and the seconds hand rotates exactly 720 ticks each nanosecond. 
        - It seems like the there are 3! = 6 potential configurations for the 
          clock hands being assigned to the three different types of hands:
          hours, minutes, and seconds.  You could probably brute force that.

    Solution ideas:
        - Take the present degree configuration of the hands and brute backtrack 
          until they're all pointing in the same direction.
            - You could further optimize by finding other configurations that are
              unique to that time, considering the arbitary axis.
            - Once you have that direction in terms of degrees/ticks, you know how
              to align the axis and tell what time the original clock configuration is.
        - After the brute force, it would be nice to have a closed-form method
          of evaluating the current state of the clock, represented as a vector.
          Is this combinatorics?
        - Determine if the current assignment of ticks and rates are divisible by the same factor.
    """
    ticks = arr
    assignable_rates = [1, 12, 720] 
    
    for rates in permute(assignable_rates):
        result = trysolvebetterokay(ticks, rates)
        if result:
            return result

    return None 

    #result = trysolve(ticks, rates)
     
    # Case #1: 0 0 0 0
    # Case #2: 6 30 0 0
    # Case #3: 1 2 3 0


def main():
    n_cases = int(input())
    for i in range(1, n_cases + 1):
        elements = [int(x) for x in input().split()]
        result = solve(elements)
        print('Case #{}: {}'.format(i, result))


main()
