#!/usr/bin/env python3
"""
Returns the first element of a sequence or None if the sequence is empty.
"""

from typing import Sequence, Any


def safe_first_element(lst: Sequence) -> Any:
    """
    Args:
        lst: A sequence first element is returned, or None if sequence is empty

    Returns:
        first element of sequence, or None if sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
