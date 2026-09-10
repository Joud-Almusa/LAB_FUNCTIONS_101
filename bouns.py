
def countdown2(n):

    """
    Returns a countdown pattern starting from n as a string.
    Each line counts down from its starting number to 1.
    """

    pattern = ""

    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            pattern += str(j) + " "

        pattern += "\n"

    return pattern


print(countdown2(5))