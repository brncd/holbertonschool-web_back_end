#!/usr/bin/env python
"""Type-annotated functions."""


from typing import Callable

def make_multiplier(multiplier: float) -> callable[[float], float]:
    """Return a function that multiplies a float by multiplier."""
    return lambda x: x * multiplier
