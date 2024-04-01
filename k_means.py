import numpy as np
import copy

def get_distance(point, center):
    if point.shape == ():
        return np.abs(center - point)
    else :
        dis = 0
        for inner_ii in range(point.size):
            dis += (point[inner_ii]-center[inner_ii])**2
        dis = np.sqrt(dis)
        return dis

def get_square(point, center):
    if point.shape == ():
        return (center - point)**2
    else :
        dis = 0
        for inner_ii in range(point.size):
            dis += (point[inner_ii]-center[inner_ii])**2
        return dis

def get_bss(array, centers, class_count):
    mean = np.mean(array, axis=0)
    bss = 0
    if centers[0].shape == ():
        for ii in range(centers.shape[0]):
            bss += class_count[ii] * (mean-centers[ii]) ** 2
    else :
        for ii in range(centers.shape[0]):
            bss_tmp = 0
            for inner_ii in range(mean.size):
                bss_tmp += (mean[inner_ii]-centers[ii][inner_ii])**2
            bss += bss_tmp * class_count[ii]
    return bss

def k_means_step(array, centers):
    step = 0
    np_array = np.array(array)
    np_centers = np.array(centers)
    centers_copy = copy.deepcopy(np_centers)
    go_ahead = True

    while go_ahead:
        dis = []
        for ii in range(np_array.shape[0]):
            tmp_dis = []
            for center in range(np_centers.shape[0]):
                tmp_dis.append(get_distance(np_array[ii], np_centers[center]))
            dis.append(tmp_dis)
        print(f"[INFO] Step = {step}, distance matrix")
        print(dis)
        np_dis = np.array(dis)
        point_class = np.argmin(np_dis, axis=1)
        print(point_class)
        new_centers = []
        class_count = []
        for ii in range(np_centers.shape[0]):
            count_ = 0
            if np_centers[0].shape == ():
                tmp_ = 0
                for jj in range(point_class.size):
                    if point_class[jj] == ii:
                        count_ += 1
                        tmp_ += np_array[jj]
            else:
                tmp_ = np.zeros(np_centers[0].shape[0])
                for jj in range(point_class.size):
                    if point_class[jj] == ii:
                        count_ += 1
                        tmp_ += np_array[jj]
            new_centers.append(tmp_/count_)
            class_count.append(count_)
        np_centers = copy.deepcopy(np.array(new_centers))
        print(f"New centers = {new_centers}")

        SSE = 0
        for ii in range(np_centers.shape[0]):
            for jj in range(point_class.size):
                if point_class[jj] == ii:
                    SSE += get_square(np_array[jj], np_centers[ii])
        print(f"SSE = {SSE}")
        BSS = get_bss(np_array, np_centers, np.array(class_count))
        print(f"BSS = {BSS}")

        if np.allclose(np_centers, centers_copy, rtol=1e-05, atol=1e-08, equal_nan=False):
            go_ahead = False
        centers_copy = copy.deepcopy(np_centers)
        step += 1
        print()
    
import argparse

CLI=argparse.ArgumentParser()
CLI.add_argument(
    "--array",
    nargs="*",
    type=float,
    default=[1, 2, 3],
)
CLI.add_argument(
    "--centers",
    nargs="*",
    type=float,
    default=[1, 2, 3],
)


args = CLI.parse_args()
#args.array = [[100,0],[ 200,0], [400,0], [800,0], [1100,0] ,[1600,0]]
#args.centers = [[1100,0],[1600,0]]
k_means_step(args.array, args.centers)

