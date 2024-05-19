#!/usr/bin/evn python3
"""Module that implements the basics of async in python"""


import random
import asyncio
from typing import Union


async def wait_random(max_delay: Union[int, float] = 10) -> float:
    """This is an asynchronous coroutine that takes an integer
    argument and waits for a random delay between 0 and max_delay seconds
    and eventually returns it"""
    delay = random.randint(0, max_delay)
    await asyncio.sleep(delay)
    return delay
