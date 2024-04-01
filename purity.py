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

purity = 0.0
for ii in range(len(args.array)//2):
    purity += args.array[ii*2] / args.array[ii*2+1] * args.array[ii*2+1] / args.array[-1]

print(f"array = {args.array}, purity = {purity}")
    

