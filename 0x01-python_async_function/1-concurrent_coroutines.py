#!/usr/bin/env python3
"""Module that executes multiple coroutines at the same time
with async
"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Function that executes the multiple coroutines at the same time
    with async
    """
    delay_list = [await wait_random(max_delay) for _ in range(n)]
    return delay_list
