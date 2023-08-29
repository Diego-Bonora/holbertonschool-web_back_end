#!/usr/bin/env python3
""" random delay between 0 and a given number """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ random delay between 0 and a given number """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
