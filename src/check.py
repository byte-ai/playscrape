import pandas as pd
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", help="app name")
ap.add_argument("-rate", "--rating", help="Rating user reviews")
ap.add_argument("-q", "--quantity", required=False, help="quantity?")

args = vars(ap.parse_args())

def check_dataset(name, star, quantity) -> None :
  df = pd.read_csv("data/" + name + "_" + star + "star.csv")
  if quantity :
    print(df.head(int(quantity)))
  else :
    print(df.head)
    

if __name__ == "__main__":
  check_dataset(args["name"], args["star"], args["quantity"])