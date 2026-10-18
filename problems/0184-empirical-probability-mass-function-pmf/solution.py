import numpy as np
def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    samples = np.array(samples)
    if len(samples) == 0:
        return []
    value, count = np.unique(samples, return_counts = True)
    l = [(int(x),c/len(samples)) for x,c in zip(value,count)]
    return l