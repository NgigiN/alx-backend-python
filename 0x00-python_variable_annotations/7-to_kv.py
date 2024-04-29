#!/usr/bin/env python3
"""
This module converts a string and int/float to a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts to tuple.
    Arguments:
    k: string
    v: int/float
    Returns
    Tuple
    """
    return [k, v*v]
