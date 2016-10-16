import requests
from bs4 import BeautifulSoup

result = requests.get("http://www.imdb.com/chart/top")

try:
    #we save the content of the page
    content = result.text
    #getting the soup
    soup = BeautifulSoup(content,"html.parser")
    #getting all divs with given class
    mydivs = soup.find_all(class_="titleColumn", text=True)
    #gettin' all text inside that class
    for title in soup.find_all(class_="titleColumn"):
        print title.text
except result.status_code != 200:
    print "Sorry, an error happened"