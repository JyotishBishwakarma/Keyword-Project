import json
import urllib.request
import requests
from mongoconntest import get_database
import xml.etree.ElementTree as ET

def amazon_scraping(query):
    url=f"https://completion.amazon.ca/api/2017/suggestions?limit=10&prefix={query}&suggestion-type=WIDGET&suggestion-type=KEYWORD&page-type=Search&alias=aps&site-variant=desktop&version=3&event=onkeypress&wc=&lop=en_CA&last-prefix=c&avg-ks-time=2696&fb=1&session-id=131-7867665-8023625&request-id=GH37EMG5ABHERT1VEZXV&mid=A2EUQ1WTGCTBG2&plain-mid=7&client-info=amazon-search-ui"
    
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    #print(result)

    mydb = get_database()
    mycol = mydb["testnewkeywrd"]

    
    for x in result['suggestions']:
        x['_id'] = x['value']
        #print(x)
        try:
            mycol.insert_one(x)
        except:
            pass
        


# Referred from 
# https://dev.to/hassancs91/develop-a-keyword-research-tool-in-minutes-python-and-c-4g32

def google_keywords(word):
        mydb = get_database()
        mycol = mydb["testnewkeywrd"]
        questionResults ={}
       
        # API Call
        googleSearchUrl = f"http://google.com/complete/search?output=toolbar&gl=COUNTRY&q={word}"

        # Call The URL and Read Data
        result = requests.get(googleSearchUrl)
        tree = ET.ElementTree(ET.fromstring(result.content))
        root = tree.getroot()
        

        for suggestion in root.findall('CompleteSuggestion'):
            question = suggestion.find('suggestion').attrib.get('data')
            print(question)
            questionResults["_id"] = question
            questionResults["value"] = question
            try:
                mycol.insert_one(questionResults)
            except:
                pass





