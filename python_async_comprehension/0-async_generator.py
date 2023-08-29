#!/usr/bin/env python3
""" yield a random number """
import random
import asyncio


async def async_generator():
    """ yield a random number """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
