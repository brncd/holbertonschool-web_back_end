#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async."""


import asyncio
from typing import List
from random import uniform


async def wait_random(max_delay: int) -> float:
    """Waits for a random delay between 0 and max_delay seconds."""
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Waits for a random delay between 0 and max_delay seconds."""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
