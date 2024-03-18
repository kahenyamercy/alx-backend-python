#!/usr/bin/env python3
"""Measure runtime module."""

import time
from typing import Callable


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the average execution time for wait_n(n, max_delay).

    Args:
        n (int): Number of coroutines to execute.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        float: Average execution time per coroutine.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
