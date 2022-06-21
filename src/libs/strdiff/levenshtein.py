import numpy as np


def distance(t: str, x: str):
    print("Compare distance", t, "----", x)
    if not t:
        return len(x)
    elif not x:
        return len(t)

    t_first, x_first = t[0], x[0]
    t_rest, x_rest = t[1:], x[1:]

    if t_first == x_first:
        return distance(t_rest, x_rest)
    else:
        return 1 + min(distance(t, x_rest),
                       distance(t_rest, x),
                       distance(t_rest, x_rest))
