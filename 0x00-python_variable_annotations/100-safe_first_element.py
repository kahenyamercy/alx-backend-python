#!/usr/bin/env python3
"""
Returns the first element of a sequence or None if the sequence is empty.
"""

from typing import Sequence, Any


def safe_first_element(lst: Sequence) -> Any:
    """
    Args:
        lst (Sequence): Input sequence.

    Returns:
        Any: The first element of sequence, or None if sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
