from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Float
from config.db import meta

room = Table(
    'room', meta,
    Column('ID', Integer, primary_key=True, autoincrement=True),
    Column('area', Float),
    Column('price', Float),
    Column('max_people', Integer),
    Column('status', Integer),
    Column('houseID', Integer, ForeignKey('boarding_house.ID'))
)
