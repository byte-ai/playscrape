from google_play_scraper import Sort, reviews, search
import pandas as pd
import numpy as np
import argparse

ap = argparse.ArgumentParser()

ap.add_argument("-s", "--star", required=True, help="star review")
ap.add_argument("-n", "--name", required=True, help="app name")
ap.add_argument("-lang", "--language", required=False, help="reviews language")
ap.add_argument("-c", "--country", required=False, help="user country")

args = vars(ap.parse_args())
print("""
                    ____                       _             
                   / ___|  ___ _ __ __ _ _ __ (_)_ __   __ _ 
                   \___ \ / __| '__/ _` | '_ \| | '_ \ / _` |
                    ___) | (__| | | (_| | |_) | | | | | (_| |
                   |____/ \___|_|  \__,_| .__/|_|_| |_|\__, |
                                        |_|            |___/ 
""")
def search_user_reviews(star, name_code) -> pd.DataFrame:
  review, _ = reviews(
      name_code,
      lang='en',
      country='us',
      sort=Sort.NEWEST,
      filter_score_with=star
  )
  df = pd.DataFrame(np.array(review), columns=['review'])
  df = df.join(pd.DataFrame(df.pop('review').tolist()))
  print("Total scraped data = ", len(review))
  return df

def search_app(star, name, language, country) -> None :
  result = search(
    name,
    lang=language,
    country=country,
    n_hits=1
  )
  name_code = ""
  for x in result: name_code = x["appId"]
  print(name_code)
  df = search_user_reviews(star, name_code)
  print(df)

  df.to_csv("data/" + name + "_" + star + "star.csv", index=False)

if __name__ == "__main__" :
  search_app(args["star"], args["name"])