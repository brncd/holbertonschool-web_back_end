#!/usr/bin/env python3
"""Tasks."""


import asyncio
from typing import List


wait_n = __import__('1-concurrent_coroutines').wait_n


def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a asyncio.Task."""
    return asyncio.run(wait_n(n, max_delay))
