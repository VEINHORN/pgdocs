def h1(value, is_newline=True):
    expr = "# " + value
    return expr + "\n" if is_newline else expr
