#!/usr/bin/env python3
"""
to_kv: a type-annotated function that takes a string k and an int OR float v
as arguments and returns a tuple.First element of tuple is the string k.
The second element is square of int/float v and should be annotated as a float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns tuple with string k and the square of the int/float v.

    Args:
        k (str): The string element.
        v (Union[int, float]): The integer or float element.

    Returns:
        Tuple[str, float]:tuple containing string k and the square of v.
    """
    return (k, float(v ** 2))
