from profiler import profile
from loguru import logger
import numpy as np
from random import randint
import math
import time


@profile
def some_task():
    logger.info("Starting Long Running Task")
    result = np.empty(5, dtype=np.float64)
    a = np.random.rand(10 ** 6)
    b = np.random.rand(10 ** 6)
    for i in range(len(result)):
        result[i] = math.exp(2.1 * a[i] + 3.2 * b[i])
        time.sleep(randint(1, 2))


if __name__ == "__main__":
    some_task()
