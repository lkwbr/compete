# function.py

# NOTE: Attempt to scale for numbers of 10^18 (i.e., 18 digits)

def tidy_numbers(*args):

    num_str = args[0]

    # TODO: Fix this brute-force solution with something more elegant that I
    # had in mind last night

    # Loop backwards through digits
    num = int(num_str)
    while True:
        if __is_tidy(str(num)): return num, ""
        num -= 1

    return num, ""

def __is_tidy(num):
    """
    Takes a string representation of a number, and determines if it's "pretty"
    """

    num_digits = map(int, list(num))
    # Okay to use, because 1 <= N
    last_digit = -1
    for digit_str in num_digits:
        this_digit = int(digit_str)
        if last_digit > this_digit: return False
        last_digit = this_digit
    return True
