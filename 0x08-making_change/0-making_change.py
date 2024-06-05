#!/usr/bin/python3
"""_Making Change_
"""


def makeChange(coins, total):
    """_makeChange method_

    Args:
        coins (_int_): _int_
        total (_int_): _int_

    Returns:
        _iny_: _int_
    """
    if total <= 0 or len(coins) == 0:
        return 0

    coins.sort(reverse=True)
    count = 0
    for i in coins:
        count += total // i
        total = total % i
    if total != 0:
        return -1
    return count
