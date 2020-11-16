#html

# using beautifulsoup module 

from bs4 import BeautifulSoup
import urllib.request as req


res = req.urlopen('http://127.0.0.1:5500')


soup= BeautifulSoup(res, 'html.parser')
# print(soup.title)
# print(soup.title.text)
# print(soup.title.getText())

# print(soup.h6)

# not unique , not working well when finding

# print(soup.div) 
# print(soup.div.next_sibling) 
# print(soup.div.next_sibling)
# print(soup.div.previous_sibling)  

# In most of the urls, there are so~ many div tags. Yet, it is int the format 
# of <div id="test0">
#print(soup.find_all(class_="myclass")) 


# finding the characterisitics of info
for tag in soup.find_all('a'):
    print(tag['href'])

