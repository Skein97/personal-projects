import requests
from bs4 import BeautifulSoup
from pprint import pprint

# Create a response variable that gets a webpage
res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')

# Use Beautiful soup to parse the webpage
soup1 = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
# Get the webpage attributes
link1 = soup1.select('.titleline > a')
link2 = soup2.select('.titleline > a')
subtext1 = soup1.select('.subtext')
subtext2 = soup2.select('.subtext')

# Add all the links together
links = link1 + link2
subtexts = subtext1 + subtext2


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom(links, subtexts):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtexts[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


for i in create_custom(links, subtexts):
    pprint(i)
