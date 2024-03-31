import numpy as np
import argparse

def cosine_similarity(x, y):
    cos_sim = np.dot(x,y)/(np.linalg.norm(x), np.linalg.norm(y))
    print(f"cos_sim = {cos_sim}")

if __name__ == "__main__":
    CLI=argparse.ArgumentParser()
    CLI.add_argument(
      "--lista",
      nargs="*",
      type=float,
      default=[1.0, 2.0, 3.0],
    )
    CLI.add_argument(
      "--listb",
      nargs="*",
      type=float,  # any type/callable can be used here
      default=[],
    )
    CLI.add_argument(
      "--method",
      choices=["cos", "min", "euc", "man", "sup"]
    )
    args = CLI.parse_args()
    x = np.array(args.lista)
    y = np.array(args.lista)

    match args.method:
    case "cos":
        cosine_similarity(x,y)
    case "min":
        cosine_similarity(x,y)
    case _:
        raise ValueError(f"args.method is not supported")



