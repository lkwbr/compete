"""
It seems like you want to consider: 
    - The initial character frequencies, and sort them descending 
    - The number of flips each unique character would take to "convince" the others to switch
        - To determine convinceability of the others, you would determine which ones are vowels and which ones are consonents (types).  For every other character, if their type is the same, the weight is 2s (1 to flip to the other type, and 1 to flip back but to the specific character).  Otherwise, the weight is 1s. 
"""


VOWELS = {'a', 'e', 'i', 'o', 'u'}


def solve(s: str) -> int:
    # Compute lookups once
    s = s.lower()
    char_stats = [
        (
            chr(ord('a') + i), 
            len([c for c in s if c == chr(ord('a') + i)]), 
            int(chr(ord('a') + i) in VOWELS)
        )
        for i in range(ord('z') - ord('a') + 1)
    ]
    char_stats = sorted(char_stats, key=lambda x: -x[1])

    # Greedily snag char requiring the least amount of "convincing" 
    # to the others.
    quickest_char = (None, None)
    for i, (c, f, is_v) in enumerate(char_stats):
        others = char_stats[:i] + char_stats[i+1:]
        other_con_freqs = sum([o_f for _, o_f, o_is_v in others if not o_is_v])
        other_vow_freqs = sum([o_f for _, o_f, o_is_v in others if o_is_v])
        #print(c, other_con_freqs, other_vow_freqs)
        char_steps = other_vow_freqs * 2 + other_con_freqs if is_v \
                     else other_vow_freqs + other_con_freqs * 2
        if not quickest_char[0] or char_steps < quickest_char[1]:
            quickest_char = (c, char_steps)
        
    return quickest_char[1]


if __name__ == '__main__':
    n = int(input())
    for i in range(1, n + 1):
        s = input()
        x = solve(s)
        print(f'Case #{i}:', x)
