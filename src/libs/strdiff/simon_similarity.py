def _get_bigrams(s):
    """
    Take a string and return a list of bigrams.
    """
    if s is None:
        return ""

    return [s[i: i + 2] for i in list(range(len(s) - 1))]


def distance(t: str, x: str):
    """
        Perform bigram comparison between two strings
        and return a percentage match in decimal form.
        """
    pairs1 = _get_bigrams(t)
    pairs2 = _get_bigrams(x)
    union = len(pairs1) + len(pairs2)

    if union == 0 or union is None:
        return 0

    hit_count = 0
    for x in pairs1:
        for y in pairs2:
            if x == y:
                hit_count += 1
                break

    similarity = (2.0 * hit_count) / union
    return (1. - similarity) * len(t)
