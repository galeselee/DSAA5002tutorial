import numpy as np
import argparse

CLI=argparse.ArgumentParser()
CLI.add_argument(
    "--array",
    nargs="*",
    type=float,
    default=[1.0, 2.0, 3.0],
)

args = CLI.parse_args()


print(f"Mean = {np.mean(args.array)}")
print(f"Var = {np.var(args.array)}")
print(f"Standard deviation = {np.sqrt(np.var(args.array))}")

zscore = []
for ii in args.array:
    zscore.append( (ii-np.mean(args.array)) / (np.sqrt(np.var(args.array))) )

print(f"z-score norlization = {zscore}")

