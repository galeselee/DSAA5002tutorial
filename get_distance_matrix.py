import numpy as np
import copy

import argparse
CLI=argparse.ArgumentParser()
CLI.add_argument(
    "--array",
    nargs="*",
    type=int,
    default=[1, 2, 3],
)

args = CLI.parse_args()

def get_distance(a, b):
    if not isinstance(a, list):
        return abs(a - b)
    else :
        dis = 0
        for inner_ii in range(len(a)):
            dis += (a[inner_ii]-b[inner_ii])**2
        dis = np.sqrt(dis)
        return dis

array = args.array

dis = np.zeros((len(array), len(array)))
for ii in range(len(array)):
    for jj in range(ii, len(array)):
        dis[ii][jj] = get_distance(array[ii], array[jj])

for ii in range(len(array)):
    for jj in range(0, ii):
        dis[ii][jj] = dis[jj][ii]

print(dis)





