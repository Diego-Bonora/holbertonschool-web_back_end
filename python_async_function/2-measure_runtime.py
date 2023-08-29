#!/usr/bin/env python3
""" calculates the time needed to execute """
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ calculates the time needed to execute """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = float(end) - float(start)
    return total_time / n
