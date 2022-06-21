from .simon_similarity import *


def reduce_noise(target: str, x: str):
    for noise in ",. '`*’":
        if noise not in target:
            x = x.replace(noise, "")
    x = x.replace('\n', " ")
    x = x.strip()
    return x


class StringDiff:
    def __init__(self, target):
        self.target = target

    def set_target(self, target):
        self.target = target

    def distance(self, x):
        preprocessed_x = reduce_noise(self.target, x)
        return distance(self.target, preprocessed_x)
