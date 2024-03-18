#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async"""

from random import uniform
import asyncio
from basic_async_syntax import wait_random  # Corrected import statement


async def wait_n(n: int, max_delay: int) -> list:
    """return list of delays in ascending order"""
    delays = [wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
