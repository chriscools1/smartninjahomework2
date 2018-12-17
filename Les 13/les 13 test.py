
from urllib import urlopen
from bs4 import BeautifulSoup


url = 'https://scrapebook22.appspot.com/'
response = urlopen(url).read()
soup = BeautifulSoup(response, 'html.parser')
print(soup.html.head.title.string)

names = []
gender = []
ages = []
cities = []
emails = []

data = {""}


for link in soup.findAll("a"):
    if link.string == "See full profile":
        person_url = url[:-1] + link["href"]
        #print person_url
        person_html = urlopen(person_url).read()
        person_soup = BeautifulSoup(person_html, 'html.parser')
        for h1 in person_soup.findAll("h1"):
            if h1.string != "Hello, ninja!":
                name = h1.string
                print name
                names.append(h1.string)
        print person_soup.find("span", attrs={"class": "email"}).string
        emails.append(person_soup.find("span", attrs={"class": "email"}).string)