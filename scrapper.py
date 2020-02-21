import requests

import bs4 as BeautifulSoup

def dataGetter():
    searchUrl = 'https://www.google.com/search?q=csquared'
    data = requests.get(searchUrl)
    response = data.text
    return response

def linkGetter(page):
   
    soup = BeautifulSoup(page)

    all_links = soup.find_all('a')

    for links in all_links:
        href = links.get('href')
        print(href)

    
    