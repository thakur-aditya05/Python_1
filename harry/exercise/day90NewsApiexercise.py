# exercise 10
# use the NewsAPI and the requests module to fetch the daily news relaed to different topics 
# go to https://newsapi.org/
# and explore the various options to build you application 
# https://newsapi.org/


import requests
import json
query=input("which type of news u are intrested in ")
url=""
r=requests.get(url)
news=json.loads(r.text)
# print(r.text)
for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("---------------------------------------------------------------------------------------------------")









