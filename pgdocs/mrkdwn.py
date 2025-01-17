"""
Contains functions which helps to create Markdown items
"""


def h1(value, is_newline=True):
    expr = "# " + value
    return expr + "\n" if is_newline else expr


def h2(value, is_newline=True):
    expr = "## " + value
    return expr + "\n" if is_newline else expr
