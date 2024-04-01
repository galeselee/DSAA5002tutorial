import numpy as np
import copy


def get_distance(a, b):
    if not isinstance(a, list):
        return abs(a - b)
    else :
        dis = 0
        for inner_ii in range(len(a)):
            dis += (a[inner_ii]-b[inner_ii])**2
        dis = np.sqrt(dis)
        return dis
dis = []

array = [

]

