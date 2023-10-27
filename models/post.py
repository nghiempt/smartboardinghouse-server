from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

post = Table(
    'post', meta,
    Column('ID', Integer, primary_key=True),
    Column('title', String(255)),
    Column('content', String(255)),
    Column('location', String(255)),
    Column('image', String(255)),
    Column('account_id', Integer, ForeignKey('account.id'))
)