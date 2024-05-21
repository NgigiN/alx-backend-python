#!/usr/bin/env python3

import asyncio


async_comprehensions = __import__('1-async_comprehension').async_comprehension


async def main():
    print(await async_comprehensions())

asyncio.run(main())
