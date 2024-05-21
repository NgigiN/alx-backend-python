#!/usr/bin/env python3
"""This module implements async comprehensions"""

import asyncio
from random import uniform
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """This corouting collects 10 random numbers using async comprehension
    then returns the 10 random numbers"""
    return [value async for value in async_generator()]
