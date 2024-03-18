#!/usr/bin/env python3
"""Tasks"""

import asyncio


task_wait_randomn = __import__('0-basic_async_syntax').wait_randomn


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Executes task_wait_random n times and returns the sorted results."""
    wait_tasks = [task_wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*wait_tasks))
