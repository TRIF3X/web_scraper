from bs4 import BeautifulSoup
import requests
import json

# Enter the URL you want to scrape
url = 'https://www2.hm.com/en_us/men/products/shirts.html'
# Perform GET request to URL, timeout in seconds; note: if timeout is omitted, the request will sit indefintely if no response.
agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
response = requests.get(url, timeout=5, headers=agent)
# Pass the response content, and our parser to the BeautifulSoup class
content = BeautifulSoup(response.content, "html.parser")

# Used to hold all our data
scrapedData = []

# Use this for loop to find HTML elements and its attributes that we want
# More information can be found on the BeautifulSoup docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
for shirt in content.findAll('div', attrs={"class": "section"}):
    scrapeObj = {
        "image": shirt.find('img', attrs={"class": "item-image"}),
    }
    scrapedData.append(scrapeObj)
    print(scrapedData)

# open with file name where you want the content to go, 'w' will be used to write to this file
# with open('menShirts.json', 'w') as outfile:
    # Convert data into JSON format
    # https://docs.python.org/3/library/json.html
    # json.dump(scrapedData, outfile)

