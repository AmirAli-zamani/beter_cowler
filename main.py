from utils.db import create_tables
import sys
from crowler import get_links
from models import Article, category


def run():
    cat = category.create(name='Game News')
    for link in get_links():
        article = Article.create(url=link, category=cat)
        print(article.id)


def show_stats():
    print(f"articles: {Article.select().count()}\t categories: {category.select().count()} ")


if __name__ == '__main__':

    if sys.argv[1] == 'create_tables':
        create_tables()
    elif sys.argv[1] == 'run':
        run()
    elif sys.argv[1] == 'stats':
        show_stats()
