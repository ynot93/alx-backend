#!/usr/bin/env python3
"""
This module deals with pagination of datasets

"""


def index_range(page, page_size):
    """
    Returns a tuple containing range of pagination params.

    """
    offset = (page - 1) * page_size
    return (offset, offset + page_size)
