#!/usr/bin/env python3
"""This is a function that measures the runtime of a function"""


import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int = 0, max_delay: int = 10) -> float:
    """A function that takes integer arguments measures
    total execution time for wait_n( and returns total_time/n
    """
    start = time.time()
    await asyncio.run(wait_n(n, max_delay))
    stop = time.time()
    total_time = stop - start
    return total_time / n
