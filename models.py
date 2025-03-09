from datetime import datetime

from peewee import SqliteDatabase, Model, CharField, TextField,\
    DateTimeField, BooleanField, ForeignKeyField

# SQLITE is not perfection
database = SqliteDatabase("posts.db")


class BaseModel(Model):
    created_time = DateTimeField(default=datetime.now())

    class Meta:
        database = database


class category(BaseModel):
    name = CharField()


class Article(BaseModel):
    url = CharField()

    title = CharField(null=True)
    body = TextField(null=True)
    is_completed = BooleanField(null=False)

    category = ForeignKeyField(category, backref='articles')
