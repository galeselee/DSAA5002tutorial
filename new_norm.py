import numpy as np
import argparse

CLI=argparse.ArgumentParser()
CLI.add_argument(
    "--array",
    nargs="*",
    type=float,
    default=[1.0, 2.0, 3.0],
)

CLI.add_argument(
    "--min",
    type=float,
)
CLI.add_argument(
    "--max",
    type=float,
)

args = CLI.parse_args()
new_min = args.min
new_max = args.max


newscore = []
for ii in args.array:
    newscore.append( ( (ii-np.min(args.array)) / (np.max(args.array) - np.min(args.array) ) )  * (new_max-new_min) + new_min)

print(f"newscore norlization = {newscore}")

