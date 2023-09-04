#!/usr/bin/env python
"""Type-annotated function sum_list."""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Take a list input_list of floats and returns their sum as a float."""
    return sum(input_list)
