import numpy as np
import argparse

def jaccard_similarity(x,y):
    intersection = len(set(x) & set(y))
    union = len(set(x) | set(y))
    print(f"jac_sim = {intersection / union}")
def cosine_similarity(x, y):
    cos_sim = np.dot(x,y)/(np.linalg.norm(x)* np.linalg.norm(y))
    print(f"cos_sim = {cos_sim}")
def euclidean_similarity(x, y):
    euc_sim = np.sqrt(np.sum((x - y) ** 2))
    print(f"euc_dis = {euc_sim}")
def manchattan_similarity(x, y):
    man_sim = np.sum(np.abs(x-y))
    print(f"man_dis = {man_sim}")
def supremum_similarity(x, y):
    sup_sim = np.max(np.abs(x-y))
    print(f"sup_dis = {sup_sim}")

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
      choices=["cos", "euc", "man", "sup"]
    )
    args = CLI.parse_args()
    x = np.array(args.lista)
    y = np.array(args.listb)

    if args.method == "cos":
        cosine_similarity(x,y)
    elif args.method == "euc":
        euclidean_similarity(x,y)
    elif args.method == "man":
        manchattan_similarity(x,y)
    else:
        supremum_similarity(x,y)
