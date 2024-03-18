#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async"""

import asyncio
from typing import List
from basic_async_syntax import wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """Return list of delays in ascending order"""
    delays = [wait_random(max_delay) for _ in range(n)]
    # Gather the results as they complete
    completed_delays = await asyncio.gather(*delays)
    return sorted(completed_delays)  # Sort the completed delays
