#!/usr/bin/env python3
""" modification of given function """
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ modification of given function """
    return [(i, len(i)) for i in lst]
