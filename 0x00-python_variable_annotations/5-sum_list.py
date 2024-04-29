#!/usr/bin/env python3
"""
  This module handles complex types - list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """This function should take a list of floats and returns
    their sum as a float
    """
    sum = 0
    for i in input_list:
        sum = sum + i

    return sum
