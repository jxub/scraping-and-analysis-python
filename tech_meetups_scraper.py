import os, requests, csv
from bs4 import BeautifulSoup
#it's python 2 b*tch
#this program will print a list of all the meetups on the page
#you can use it to get any meetoups that you want, just change the url
url = "https://www.meetup.com/find/?allMeetups=true&radius=Infinity&metaCategory=tech"
tech_meetups = requests.get(url)

content = tech_meetups.text

#let's parse the sh*t out of it
soup = BeautifulSoup(content, "html.parser")

#selects the list of all the meetups
meetup_page = soup.find_all("div", {"id": "C_pageBody"})

def main():
    for meetup in meetup_page:
        meetups = meetup.find_all("a", {"class":"display-none"})
        for el in meetups:
            print el.text
        meetups_count = len(meetups)
        number = str(meetups_count)
        print "There are " + number + " meetups on the page"
    return

if __name__ == "__main__":
    main()