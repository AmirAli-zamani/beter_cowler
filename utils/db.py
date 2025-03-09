from models import Article, category, database


def create_tables():
    database.create_tables([Article, category])

