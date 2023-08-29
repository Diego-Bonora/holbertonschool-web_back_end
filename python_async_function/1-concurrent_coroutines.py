#!/usr/bin/env python3
""" returns a list of delays """
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ returns a list of delays """
    float_list: List[float] = []
    for i in range(n):
        float_list.append(await wait_random(max_delay))
    return sorted(float_list)
