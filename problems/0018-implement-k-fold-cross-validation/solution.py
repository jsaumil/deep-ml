import numpy as np
from typing import List, Tuple

def k_fold_cross_validation(n_samples: int, k: int = 5, shuffle: bool = True) -> List[Tuple[List[int], List[int]]]:
    samples = np.arange(n_samples)

    if shuffle:
        np.random.shuffle(samples)

    folds = np.array_split(samples,k)
    results = []
    for i in range(k):
        test = folds[i]
        train = np.concatenate([folds[j] for j in range(k) if j != i])

        results.append((train.tolist(),test.tolist()))
    return results