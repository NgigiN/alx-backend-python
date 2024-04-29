#!/usr/bin/env python3
"""
Correctly annotating a function's paramenters and return values
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Function taking a list as an iterable sequence
    and returns a list
    """
    return [(i, len(i)) for i in list]
