#!/usr/bin/env python3
"""Tasks"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_randomn = __import__('3-tasks').task_wait_randomn


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Return list of delays in ascending order"""
    delays = [task_wait_randomn(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
