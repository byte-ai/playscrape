import pandas as pd
import matplotlib.pyplot as plt
import argparse
from wordcloud.wordcloud import WordCloud, STOPWORDS
ap = argparse.ArgumentParser()

ap.add_argument("-d", "--data", required=True, help="Your Dataset")

args = vars(ap.parse_args())

def create_wordcloud(dataset) :
  df = pd.read_csv("data/" + dataset + ".csv")
  comment_words = ""
  stopwords = set(STOPWORDS)
  
  for val in df.content :
    val = str(val)
    
    # split the value
    tokens = val.split()
    
    for i in range(len(tokens)) :
      tokens[i] = tokens[i].lower()
    
    comment_words += " ".join(tokens) + " "
    
  words_cloud = WordCloud(width = 800, height = 800,
                background_color ='black',
                stopwords = stopwords,
                min_font_size = 10).generate(comment_words)

  plt.figure(figsize = (8, 8), facecolor = None)
  plt.imshow(words_cloud)
  plt.axis("off")
  plt.tight_layout(pad = 0)
  
  plt.show()

if __name__ == "__main__" :
  create_wordcloud(args["data"])