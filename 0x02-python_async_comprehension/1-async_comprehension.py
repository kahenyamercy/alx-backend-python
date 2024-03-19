#!/usr/bin/env python3
"""Async Comprehension"""

import random
import asyncio

from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> list[float]:
    """Async Comprehension"""
    return [num async for num in async_generator()]
