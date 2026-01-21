import numpy as np

def entropy(values):
    probs = np.abs(values) / np.sum(np.abs(values))
    return -np.sum(probs * np.log(probs + 1e-9))