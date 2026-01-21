import numpy as np

def run():
    x = np.random.rand(200)
    y = 3 * x + np.random.normal(0, 0.2, 200)
    return {
        "correlation": float(np.corrcoef(x, y)[0, 1]),
        "variance": float(np.var(y))
    }