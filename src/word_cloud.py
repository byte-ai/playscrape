import tkinter
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
import argparse
from wordcloud.wordcloud import WordCloud, STOPWORDS
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory


ap = argparse.ArgumentParser()

ap.add_argument("-d", "--name", required=True, help="Your Dataset")
ap.add_argument("-s", "--star", required=True, help="User reviews star")
ap.add_argument("-l", "--language", required=True, help="Language user use")

args = vars(ap.parse_args())

def create_wordcloud(name, star, language) -> None :
  stop_factory = StopWordRemoverFactory()
  STOPWORD = stop_factory.get_stop_words() + list(STOPWORDS)
  df = pd.read_csv("../data/" + name + "_" + star + "star_" + language +  ".csv")
  comment_words = ""
  stopwords = set(STOPWORD)
  
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
  create_wordcloud(args["name"], args["star"], args["language"])
