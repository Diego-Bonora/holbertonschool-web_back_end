#!/usr/bin/env python3
""" adds floats from a list """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ returns the addition of a list of floats """
    new_float: float = 0.0
    for num in input_list:
        new_float += num
    return new_float
