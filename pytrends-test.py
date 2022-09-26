import pandas as pd                        
from pytrends.request import TrendReq
pytrend = TrendReq()

def keywordSuggestion(keywrd):
    # Get Google Keyword Suggestions
    keywords = pytrend.suggestions(keyword=keywrd)
    df = pd.DataFrame(keywords)
    df.drop(columns=['mid'], axis=1)   # This column makes no sense
    print(df.head(20))


keywordSuggestion("dog")
