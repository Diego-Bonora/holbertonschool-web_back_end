#!/usr/bin/env python3
""" returns a new function """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns a new function """
    def multiply(multiply: float) -> float:
        return multiplier * multiply
    return multiply
