#!/usr/bin/env python3
"""Tasks"""

import asyncio


task_wait_random = __import__('3-task.py').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Executes task_wait_random n times and returns the sorted results."""
    wait_tasks = [task_wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*wait_tasks))
