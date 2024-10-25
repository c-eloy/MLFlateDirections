import tensorflow as tf 

def V_5d_1(x):
    """Constructed by Camille. Should be a line"""
    x1,x2,x3,x4,x5 = tf.split(x,5,axis=1)
    return 29 * (x1 ** 2) + 41.66666666666667 * (x1 ** 3) + 81 * (x1 ** 4) -36 * x1 * x2 + 540 * (x1 ** 3) * x2 + 20 * (x2 ** 2) + 1350 * (x1 ** 2) * (x2 ** 2) + 1500 * x1 * (x2 ** 3) + 625 * (x2 ** 4) + 32 * x1 * x3 -50 * (x1 ** 2) * x3 + 324 * (x1 ** 3) * x3 + 1620 * (x1 ** 2) * x2 * x3 + 2700 * x1 * (x2 ** 2) * x3 + 1500 * (x2 ** 3) * x3 + 20 * (x3 ** 2) + 20 * x1 * (x3 ** 2) + 486 * (x1 ** 2) * (x3 ** 2) + 1620 * x1 * x2 * (x3 ** 2) + 1350 * (x2 ** 2) * (x3 ** 2) -2.666666666666667 * (x3 ** 3) + 324 * x1 * (x3 ** 3) + 540 * x2 * (x3 ** 3) + 81 * (x3 ** 4) -4 * x1 * x4 -25 * (x1 ** 2) * x4 -540 * (x1 ** 3) * x4 + 40 * x2 * x4 -2700 * (x1 ** 2) * x2 * x4 -4500 * x1 * (x2 ** 2) * x4 -2500 * (x2 ** 3) * x4 + 40 * x3 * x4 + 20 * x1 * x3 * x4 -1620 * (x1 ** 2) * x3 * x4 -5400 * x1 * x2 * x3 * x4 -4500 * (x2 ** 2) * x3 * x4 -4 * (x3 ** 2) * x4 -1620 * x1 * (x3 ** 2) * x4 -2700 * x2 * (x3 ** 2) * x4 -540 * (x3 ** 3) * x4 + 40 * (x4 ** 2) + 5 * x1 * (x4 ** 2) + 1350 * (x1 ** 2) * (x4 ** 2) + 4500 * x1 * x2 * (x4 ** 2) + 3750 * (x2 ** 2) * (x4 ** 2) -2 * x3 * (x4 ** 2) + 2700 * x1 * x3 * (x4 ** 2) + 4500 * x2 * x3 * (x4 ** 2) + 1350 * (x3 ** 2) * (x4 ** 2) -0.3333333333333333 * (x4 ** 3) -1500 * x1 * (x4 ** 3) -2500 * x2 * (x4 ** 3) -1500 * x3 * (x4 ** 3) + 625 * (x4 ** 4) + 8 * x1 * x5 + 200 * (x1 ** 2) * x5 + 216 * (x1 ** 3) * x5 -16 * x2 * x5 + 1080 * (x1 ** 2) * x2 * x5 + 1800 * x1 * (x2 ** 2) * x5 + 1000 * (x2 ** 3) * x5 -8 * x3 * x5 -160 * x1 * x3 * x5 + 648 * (x1 ** 2) * x3 * x5 + 2160 * x1 * x2 * x3 * x5 + 1800 * (x2 ** 2) * x3 * x5 + 32 * (x3 ** 2) * x5 + 648 * x1 * (x3 ** 2) * x5 + 1080 * x2 * (x3 ** 2) * x5 + 216 * (x3 ** 3) * x5 -24 * x4 * x5 -80 * x1 * x4 * x5 -1080 * (x1 ** 2) * x4 * x5 -3600 * x1 * x2 * x4 * x5 -3000 * (x2 ** 2) * x4 * x5 + 32 * x3 * x4 * x5 -2160 * x1 * x3 * x4 * x5 -3600 * x2 * x3 * x4 * x5 -1080 * (x3 ** 2) * x4 * x5 + 8 * (x4 ** 2) * x5 + 1800 * x1 * (x4 ** 2) * x5 + 3000 * x2 * (x4 ** 2) * x5 + 1800 * x3 * (x4 ** 2) * x5 -1000 * (x4 ** 3) * x5 + 4 * (x5 ** 2) + 320 * x1 * (x5 ** 2) + 216 * (x1 ** 2) * (x5 ** 2) + 720 * x1 * x2 * (x5 ** 2) + 600 * (x2 ** 2) * (x5 ** 2) -128 * x3 * (x5 ** 2) + 432 * x1 * x3 * (x5 ** 2) + 720 * x2 * x3 * (x5 ** 2) + 216 * (x3 ** 2) * (x5 ** 2) -64 * x4 * (x5 ** 2) -720 * x1 * x4 * (x5 ** 2) -1200 * x2 * x4 * (x5 ** 2) -720 * x3 * x4 * (x5 ** 2) + 600 * (x4 ** 2) * (x5 ** 2) + 170.6666666666667 * (x5 ** 3) + 96 * x1 * (x5 ** 3) + 160 * x2 * (x5 ** 3) + 96 * x3 * (x5 ** 3) -160 * x4 * (x5 ** 3) + 16 * (x5 ** 4)

def V_10d_1(x):
    """Constructed by Camille. The polynomial of the valley is x1 + x2 + x3**2 + 4 x4**2 = 0"""
    x1,x2,x3,x4,x5, x6, x7, x8, x9, x10 = tf.split(x,10,axis=1)
    return 0.5 * (x1 ** 3) + x10 ** 4 + 1.5 * (x1 ** 2) * x2 + 1.5 * x1 * (x2 ** 2) + 0.5 * (x2 ** 3) + 1.5 * (x1 ** 2) * (x3 ** 2) + 3 * x1 * x2 * (x3 ** 2) + 1.5 * (x2 ** 2) * (x3 ** 2) + 1.5 * x1 * (x3 ** 4) + 1.5 * x2 * (x3 ** 4) + 0.5 * (x3 ** 6) + 6 * (x1 ** 2) * (x4 ** 2) + 12 * x1 * x2 * (x4 ** 2) + 6 * (x2 ** 2) * (x4 ** 2) + 12 * x1 * (x3 ** 2) * (x4 ** 2) + 12 * x2 * (x3 ** 2) * (x4 ** 2) + 6 * (x3 ** 4) * (x4 ** 2) + 24 * x1 * (x4 ** 4) + 24 * x2 * (x4 ** 4) + 24 * (x3 ** 2) * (x4 ** 4) + 32 * (x4 ** 6) + x5 ** 4 + x6 ** 4 + x7 ** 4 + x8 ** 4 + x9 ** 4

def V_10d_2(x):
    """Same as before but there is an change of variables in it"""
    x1,x2,x3,x4,x5, x6, x7, x8, x9, x10 = tf.split(x, 10, axis = 1)
    return (x3 + x5 + x7) ** 4 + (-x1 + x10 -x3 + x4 -x5 -x7 + x8) ** 4 + 0.5 * ((x10 -x2 + x5 -x6 -x8 + 4 * ((x1 + x2 -x4 -x6 -x7 + x8) ** 2) + (-x1 + x2 -x5 -x6 + x7 + x8 -x9) ** 2) ** 3) + (-x3 -x4 + x5 -x6 -x9) ** 4 + (-x1 + x2 + x3 + x4 + x5 -x6 -x7 -x8 -x9) ** 4 + (x1 + x10 -x2 -x6 + x8 -x9) ** 4 + (x1 + x3 + x4 + x5 + x6 + x8 + x9) ** 4

