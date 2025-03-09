import requests
from bs4 import BeautifulSoup
from models import Article


def crawl_page(url):
    print(url)
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        heder_div = soup.find('div', attrs={'id': 'dailyNewsPageHead'})
        title = heder_div.find('h1')
        body = soup.select_one('')
    elif requests.status_codes != 200:
        raise


def get_links():
    response = requests.get('https://vigiato.net')
    links = list()
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a'):
            links.append(link.attrs.get('href'))

    elif requests.status_codes != 200:
        print("")

    return links


if __name__ == "__main__":
    articles = Article.select().where(Article.is_completed == False)

    for article in articles:
        try:
            crawl_page(article.url)
        except:
            article.is_completed = True
            article.save()
