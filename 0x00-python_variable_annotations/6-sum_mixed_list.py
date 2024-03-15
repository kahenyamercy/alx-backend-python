#!/usr/bin/env python3
"""
sum_mixed_list: a type-annotated function that takes a list mxd_lst of integers
and floats and returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of integers and floats.

    Args:
        mxd_lst(List[Union[int, float]]):list of integers and floats to sum.

    Returns:
        float: The sum of the integers and floats in the input list.
    """
    return sum(mxd_lst)
