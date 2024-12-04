
import tensorflow as tf
import numpy as np

dim = 4

def V(x):
    """
    V = ((-1 + x2 ** 2 -2 * x2 * x3 + x3 ** 2 + 2 * x2 * x4 -2 * x3 * x4 + 2 * (x4 ** 2)) ** 2) * ((x1 ** 3 + 2 * (x2 ** 3) -x3 + 2 * (x3 ** 3) -x4 + 6 * (x3 ** 2) * x4 + 6 * x3 * (x4 ** 2) + 2 * (x4 ** 3) + 6 * (x2 ** 2) * (x3 + x4) + 3 * (x1 ** 2) * (x2 + x3 + x4) + x2 * (-1 + 6 * (x3 ** 2) + 12 * x3 * x4 + 6 * (x4 ** 2)) + x1 * (-1 + 4 * (x2 ** 2) + 4 * (x3 ** 2) + 8 * x3 * x4 + 4 * (x4 ** 2) + 8 * x2 * (x3 + x4))) ** 2)
    """

    x1, x2, x3, x4 = tf.split(x, 4, axis=1)

    return ((-1 + x2 ** 2 -2 * x2 * x3 + x3 ** 2 + 2 * x2 * x4 -2 * x3 * x4 + 2 * (x4 ** 2)) ** 2) * ((x1 ** 3 + 2 * (x2 ** 3) -x3 + 2 * (x3 ** 3) -x4 + 6 * (x3 ** 2) * x4 + 6 * x3 * (x4 ** 2) + 2 * (x4 ** 3) + 6 * (x2 ** 2) * (x3 + x4) + 3 * (x1 ** 2) * (x2 + x3 + x4) + x2 * (-1 + 6 * (x3 ** 2) + 12 * x3 * x4 + 6 * (x4 ** 2)) + x1 * (-1 + 4 * (x2 ** 2) + 4 * (x3 ** 2) + 8 * x3 * x4 + 4 * (x4 ** 2) + 8 * x2 * (x3 + x4))) ** 2)