#!/usr/bin/env python3
"""
make_multiplier: a type-annotated function that takes float multiplier
as an argument and returns function that multiplies a float by multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns function that multiplies float by the given multiplier.

    Args:
        multiplier (float): The multiplier to be used.

    Returns:
        Callable[[float], float]:function that multiplies float by multiplier.
    """
    def multiplier_function(num: float) -> float:
        """
        Multiplies a float by the given multiplier.

        Args:
            num (float): The number to be multiplied.

        Returns:
            float: The result of multiplying the number by the multiplier.
        """
        return num * multiplier

    return multiplier_function
