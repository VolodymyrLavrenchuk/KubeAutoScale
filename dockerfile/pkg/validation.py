# -*- coding: utf-8 -*-
"""Validations."""

def validate(expression, message):
    """Validate expression."""
    try:
        assert expression
    except AssertionError as error:
        error.args += (message,)
        raise