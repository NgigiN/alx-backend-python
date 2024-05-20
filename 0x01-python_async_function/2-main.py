#!/usr/bin/env python3

import asyncio
measure_time = __import__('2-measure_runtime').measure_time

n = 5
max_delay = 9


async def main():
    avg_time = await measure_time(n, max_delay)
    print(f"Average time per call: {avg_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())
