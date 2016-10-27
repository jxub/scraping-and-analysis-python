import requests #for url get
from bs4 import BeautifulSoup #to parse html
from textblob import TextBlob #to analyse sentiments

"""
***********************
***the other SCRAPER***
***********************
Gets html from *ehem*IMDB*ehem* and scrapes the comments
"""

#AFTER 8APROX 8 GET REQUESTS TO THE SAME PAGE, REQUESTS GET DENIED
#THEN CHANGE URL

#the first page has different url structure
first_url = 'http://www.imdb.com/title/tt0468569/reviews?ref_=tt_ql_3'

def first_page_ratings():
    r = requests.get(first_url)

    try:
        soup = BeautifulSoup(r.text, "lxml")
        title_link = soup.find_all("a", class_="main", text=True)
        for title in title_link:
            movie_title = title.text
        raw_comments = soup.find_all("p")
        polarity = []
        subjectivity = []
        stats()


    except requests.ConnectionError:
        print("IMDB has just fucked you in the ass! Change the URL...")
    other_pages_ratings()


def other_pages_ratings():
    urls = []
    #next pages are all the same
    root = 'http://www.imdb.com/title/tt0111161/reviews?start='
    for number in range(10, 110, 10):
        page_url = root+str(number)
        urls.append(page_url)
        sentiment_analyzer(page_url)


def sentiment_analyzer(page_url):
    try:
        r = requests.get(page_url)
        soup = BeautifulSoup(r.text, "lxml")
        title_link = soup.find_all("a", class_="main", text=True)
        for title in title_link:
            movie_title = title.text
        raw_comments = soup.find_all("p")
        polarity = []
        subjectivity = []
        stats()

    except requests.ConnectionError:
        print("IMDB has just f*cked you in the a$$! Change the URL...")

def stats():
    for raw_comment in raw_comments:
        count = 0
        blob = raw_comment.text
        testimonial = TextBlob(blob)
        if testimonial.sentiment.polarity != 0 and testimonial.sentiment.subjectivity != 0:
            count += 1
            polarity.append(testimonial.sentiment.polarity)
            subjectivity.append(testimonial.sentiment.subjectivity)
    medium_polarity = reduce(lambda x, y: x + y, polarity) / len(polarity)
    medium_subjectivity = reduce(lambda x, y: x + y, subjectivity) / len(subjectivity)
    print("Stats for " + str(movie_title))
    print("medium polarity: " + str(medium_polarity))
    print("medium subjectivity: " + str(medium_subjectivity))
    print('polarity of all the ratings')
    print(polarity)
    print('subjectivity of all the ratings')
    print(subjectivity)

if __name__ == "__main__":
    first_page_ratings()
