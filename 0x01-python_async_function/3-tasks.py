#!/usr/bin/env python3
"""Module to create an asyncio.Task for wait_random from basic_async_syntax."""

import asyncio
from typing import Task
from basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> Task:
    """Create and return an asyncio.Task for wait_random(max_delay).

    Args:
        max_delay (int): The maximum delay for the wait_random coroutine.

    Returns:
        asyncio.Task:asyncio task representing the execution of wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
