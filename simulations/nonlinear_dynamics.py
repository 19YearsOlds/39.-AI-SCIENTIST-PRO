import numpy as np

def run():
    x = np.random.rand(200)
    y = x**2 + np.sin(5 * x) + np.random.normal(0, 0.1, 200)
    return {
        "correlation": float(np.corrcoef(x, y)[0, 1]),
        "variance": float(np.var(y))
    }