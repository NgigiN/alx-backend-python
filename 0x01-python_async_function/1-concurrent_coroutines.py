#!/usr/bin/env python3
"""Module that executes multiple coroutines at the same time
with async
"""
from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Function that executes the multiple coroutines at the same time
    with async
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delay_list = [await task for task in asyncio.as_completed(tasks)]
    return delay_list
