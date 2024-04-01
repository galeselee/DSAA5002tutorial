import numpy as np
import copy
import argparse
import math
import sys

# one dim, min/max
def p2p_distance(a, b, method):
    dis = -1
    if method == "min":
        if isinstance(a, list):
            if isinstance(b, list):
                min_dis = 9999999999
                for ii in a:
                    for jj in b:
                        min_dis = min(abs(jj-ii), min_dis)
                dis = min_dis
            else :
                min_dis = 9999999999
                for ii in a:
                    min_dis = min(abs(b-ii), min_dis)
                dis = min_dis
        else :
            if isinstance(b, list):
                min_dis = 999999999
                for jj in b:
                    min_dis = min(abs(jj-a), min_dis)
                dis = min_dis
            else :
                dis = abs(b-a)
    elif method == "max":
        if isinstance(a, list):
            if isinstance(b, list):
                max_dis = 0
                for ii in a:
                    for jj in b:
                        max_dis = max(abs(jj-ii), max_dis)
                dis = max_dis
            else :
                max_dis = 0
                for ii in a:
                    max_dis = max(abs(b-ii), max_dis)
                dis = max_dis
        else :
            if isinstance(b, list):
                max_dis = 0
                for jj in b:
                    max_dis = max(abs(jj-a), max_dis)
                dis = max_dis
            else :
                dis = abs(b-a)
    return dis

def get_distance(array, method):
    dis = np.zeros((len(array), len(array)))
    for ii in range(len(array)):
        for jj in range(ii+1, len(array)):
            dis[ii][jj] = p2p_distance(array[ii], array[jj], method)

    for ii in range(len(array)):
        for jj in range(0,ii):
            dis[ii][jj] = dis[jj][ii]
    for ii in range(len(array)):
        dis[ii][ii] = sys.maxsize


    return dis

def merge(ii,jj):
    ret_list = []
    if isinstance(ii, list):
        if isinstance(jj,list):
            ii = ii + jj
            ret_list = ii
        else:
            ii.append(jj)
            ret_list = ii
    else:
        if isinstance(jj, list):
            jj.append(ii)
            ret_list = jj
        else:
            ret_list = [ii, jj]
    return ret_list

def update_array(array, dis):
    size = len(array)
    min_dis_row = np.argmin(dis) // size
    min_dis_col = np.argmin(dis) % size
    new_array = []
    for ii in range(len(array)):
        if ii == min_dis_row:
            new_array.append(merge(array[min_dis_row], array[min_dis_col]))
        elif ii == min_dis_col:
            continue
        else:
            new_array.append(array[ii])
    return new_array


def cluster_step(array, method):
    step = 0
    class_count = array.size

    while class_count > 1:
        dis = get_distance(array, method)
        print(f"[INFO] Step = {step}, distance matrix")
        print(dis)
        np_dis = np.array(dis)
        array = update_array(array, dis)
        print(f"new array")
        print(array)
        class_count -= 1
        step += 1

if __name__ == "__main__":
    CLI=argparse.ArgumentParser()
    CLI.add_argument(
        "--array",
        nargs="*",
        type=float,
        default=[1, 2, 3],
    )
    CLI.add_argument(
      "--method",
      choices=["min", "max"]
    )

    args = CLI.parse_args()

    cluster_step(np.array(args.array), args.method)

