import random

def capture() -> list[float]:
    return [random.uniform(-1, 1) for _ in range(1024)]
