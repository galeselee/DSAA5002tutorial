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

entropy = 0.0

for ii in args.array:
    p = ii / total_num
    entropy = entropy - p * np.log2(p)

print(f"array = {args.array}, entropy = {entropy}")

