from google_play_scraper import Sort, reviews, search
import pycountry
import pandas as pd
import numpy as np
import argparse

ap = argparse.ArgumentParser(
		prog="scrape",
		description="Scraping play store reviews",
		epilog="Thanks for using this tool"
	)

ap.add_argument("-n", "--name", required=True, help="Application name")
ap.add_argument("-r", "--rating", required=True, help="Application rating based on user reviews")
ap.add_argument("-l", "--language", required=True, help="Users reviews language")

args = vars(ap.parse_args())

print("""
                    ____                       _             
                   / ___|  ___ _ __ __ _ _ __ (_)_ __   __ _ 
                   \___ \ / __| '__/ _` | '_ \| | '_ \ / _` |
                    ___) | (__| | | (_| | |_) | | | | | (_| |
                   |____/ \___|_|  \__,_| .__/|_|_| |_|\__, |
                                        |_|            |___/ 
""")

# get play store reviews app and store to df 
def search_user_reviews(star, name_code, languages) -> pd.DataFrame:
  try :
		  lang = pycountry.languages.get(name=languages).alpha_2
  except :
		  evaluation.message('LanguageIdentify', 'langnotfound', String(code))
		  return Symbol("$Failed")


  review, _ = reviews(
      name_code,
      lang,
      sort=Sort.MOST_RELEVANT,
      filter_score_with=star
  )
  df = pd.DataFrame(np.array(review), columns=['review'])
  df = df.join(pd.DataFrame(df.pop('review').tolist()))
  df.drop(['userImage', 'score', 'thumbsUpCount', 'at', 'replyContent', 'repliedAt'], inplace=True, axis=1)

  print("Total scraped data = ", len(review))
  return df

def search_app(star, name, languages) -> None :
  result = search(
    name,
    n_hits=1 # most relate information
  )
  name_code = ""
  for x in result: name_code = x["appId"]

  df = search_user_reviews(star, name_code, languages)
  df.to_csv("../data/" + name + "_" + star + "star" + "_" + languages + ".csv", index=False)

if __name__ == "__main__" :
	search_app(args["rating"], args["name"], args["language"])
