#!/usr/bin/env python3
"""Tasks."""


import asyncio
from typing import List


wait_n = __import__('1-concurrent_coroutines').wait_n


def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns the list of all the delays."""
    start_time = asyncio.get_event_loop().time()
    delays = asyncio.run(wait_n(n, max_delay))
    total_time = asyncio.get_event_loop().time() - start_time
    return [total_time / n for i in range(n)]
