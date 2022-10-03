from scraping import amazon_scraping
from scraping import google_keywords
from mongoconntest import get_database

import pandas as pd
import json

def keywordsuggest(word):
    amazon_scraping(word)
    google_keywords(word)
    mydb = get_database()
    mycol = mydb["testnewkeywrd"]
    word2 = word.replace("%20"," ")

    myquery = { "value": {"$regex":f".*{word2}.*"} }

    mydoc = mycol.find(myquery)
    print(f"testmydoc {mydoc}")
    list_cur = list(mydoc)
    df = pd.DataFrame(list_cur) 
    print(df)
    df_json =  df.to_json(orient='records')
    print(df_json)
    
    with open("data/amazon.json","w") as outfile:
        outfile.write(df_json)







