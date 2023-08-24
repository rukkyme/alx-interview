#!/usr/bin/python3
"""validUtf8 module"""


def validUTF8(data):
    """method that determines if given data represents valid UTF-8 encoding
    Args:
        data: list of integers
    Returns:
        True if valid UTF-8 encoding, else it returns False
    """
    n_bytes = 0

    # checks if the most significant bit is set or not
    mask1 = 1 << 7
    # checks if the second most significant bit is set or not
    mask2 = 1 << 6
    for num in data:
        mask = 1 << 7
        if n_bytes == 0:
            while mask & num:
                n_bytes += 1
                mask = mask >> 1
            if n_bytes == 0:
                continue

            if n_bytes == 1 or n_bytes > 4:
                return False
        else:

            if not (num & mask1 and not (num & mask2)):
                return False
        n_bytes -= 1
    return n_bytes == 0
