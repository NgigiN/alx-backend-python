#!/usr/bin/env python3
"""This module is for more involved type annotations"""
from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, type(None)] = None) -> Union[Any, T]:
    """This function requires more type annotations"""
    if key in dct:
        return dct[key]
    else:
        return default
