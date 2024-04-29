#!/usr/bin/env python3
"""
  This module that takes an argument and returns a function
"""
from typing import Callable


def mux(multiplier: float) -> Callable[[float], float]:
    """This function does the actual multiplication"""
    def multiplier_func(value: float) -> float:
        return multiplier * value
    return multiplier_func


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function takes one argument multiplier and
    returns a function that multiplies a float by multiplier
    """
    return mux(multiplier)
