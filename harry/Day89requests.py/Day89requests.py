# web pages ko scrap 
# html parsing and usse contant 
# pip3 install requests 

# simple si get requests bheji gayi hai link t ke through 
import requests
response=requests.get("https://www.google.com")
print(response)



# https://jsonplaceholder.typicode.com/ for requests apis
# /posts for post requests 
# https://jsonplaceholder.typicode.com/guide/.  

import requests
url="https://jsonplaceholder.typicode.com/posts"
data={
    "title":"harry",
    "body":"bhai",
    "userId":12,
}
headers={
    'Content-type' : 'application/json ; charset=UTF-8',
}
response=response.post(url,headers=headers,json=data)
print(response.text) 



# static pages scrapping 

# to get html source code
import requests
url="https://codewith harry.com/blogpost/django-cheatsheet"
r=requests.get(url)
print(r.text) # html source code 

# downlload 
from bs4 import BeautifulSoup
soup=BeautifulSoup(r.text,'html.parser')
print(soup.prettify())






# to get html source code
import requests
url="https://codewith harry.com/blogpost/django-cheatsheet"
r=requests.get(url)
print(r.text) # html source code 

# download 
from bs4 import BeautifulSoup
soup=BeautifulSoup(r.text,'html.parser')

# to get only "h2" headlines 
for heading in soup.find_all("h2"):
    print(heading.text)










