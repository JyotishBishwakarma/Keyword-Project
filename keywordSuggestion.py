from scraping import amazon_scraping
from mongoconntest import get_database
import pandas as pd
import json
def keywordsuggest(word):
    amazon_scraping(word)
    mydb = get_database()
    mycol = mydb["testnewkeywrd"]

    myquery = { "value": {"$regex":f"^{word}"} }

    mydoc = mycol.find(myquery)
    print(f"testmydoc {mydoc}")
    list_cur = list(mydoc)
    df = pd.DataFrame(list_cur) 
    print(df)
    df_json =  df.to_json(orient='records')
    print(df_json)
    
    with open("data/amazon.json","w") as outfile:
        outfile.write(df_json)

keywordsuggest('ma')





