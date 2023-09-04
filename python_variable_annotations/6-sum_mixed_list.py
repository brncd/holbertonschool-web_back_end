#!/usr/bin/env python
"""Type-annotated function sum_mixed_list."""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Take a list of integers and floats and returns their sum as a float."""
    return sum(mxd_lst)
