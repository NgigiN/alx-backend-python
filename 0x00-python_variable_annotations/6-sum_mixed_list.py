#!usr/bin/env python3
"""
  This module shakes it up and takes complex types: a mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    This function returns the sum of a list of floats and integers
    """
    return sum(mxd_lst)
