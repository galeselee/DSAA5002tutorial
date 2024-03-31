import numpy as np
import argparse

CLI=argparse.ArgumentParser()
CLI.add_argument(
    "--array",
    nargs="*",
    type=int,
    default=[1, 2, 3],
)

args = CLI.parse_args()

total_num = np.sum(args.array)

gini = 1

for ii in args.array:
    p = ii / total_num
    gini = gini - p**2

print(f"array = {args.array}, gini = {gini}")

