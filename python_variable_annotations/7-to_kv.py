#!/usr/bin/env python3
""" returns a tuple with the str and the square of v """
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ returns a tuple with the str and the square of v """
    return (k, float(v**2))
