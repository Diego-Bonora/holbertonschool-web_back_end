#!/usr/bin/env python3
""" adds floats and lists from a list """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """ returns the addition of a list of floats and ints """
    new_float: float = 0.0
    for num in mxd_lst:
        new_float += num
    return new_float
