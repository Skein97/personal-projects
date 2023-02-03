import requests
from bs4 import BeautifulSoup

# Create a response variable that gets a webpage
res = requests.get('https://news.ycombinator.com/news')

# Use Beautiful soup to parse the webpage
soup = BeautifulSoup(res.text, 'html.parser')
# Select parts of webpage
links = soup.select('.titleline')
votes = soup.select('.score')

def create_custom(links, votes):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        hn.append(href)
    return hn

print(create_custom(links, votes))