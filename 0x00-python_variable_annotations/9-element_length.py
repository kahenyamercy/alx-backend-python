#!/usr/bin/env python3
"""
Returns list of tuples,each containing an element from input list and length.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Args:
        lst (Iterable[Sequence]): Input list of sequences.

    Returns:
        List[Tuple[Sequence,int]]
    """
    return [(i, len(i)) for i in lst]
