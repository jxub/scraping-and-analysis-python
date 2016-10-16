from bs4 import BeautifulSoup
import requests


#we make a request to the spacified web
result = requests.get("http://shop.oreilly.com/category/early-release.do")

#define a function that does the magic
def scraper():
    #we save the content of the page
    c = result.content
    #parsing the samples
    soup = BeautifulSoup(c,"html.parser")
    samples = soup.find_all('a', href=True, id="search-inside")
    #saving'em in a dict
    data = {}
    for a in samples:
        title = a.string.strip()
        data[title] = a.attrs['href']
    print data

#we check if we get a response
if result.status_code == 200:
    scraper()
    