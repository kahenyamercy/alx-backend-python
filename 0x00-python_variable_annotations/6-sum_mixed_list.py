#!/usr/bin/env python3
"""
sum of a mixed list of floats and integers.
"""

from typing import List, Union


def sum_mixed(numbers: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of floats.

    Args:
        numbers (List[Union[int, float]]): The list of floats to sum.

    Returns:
        float: The sum of the floats in the input list.
    """
    return sum(numbers)
