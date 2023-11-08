from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Float, String
from config.db import meta

room = Table(
    'sbh_apis_room', meta,
    Column('ID', Integer, primary_key=True, autoincrement=True),
    Column('room_number', Integer),
    Column('area', Float),
    Column('max_people', Integer),
    Column('status', Integer),
    Column('contract', String(255)),
    Column('price', Integer),
    Column('house_ID', Integer, ForeignKey('sbh_apis_boarding_house.ID'))
)
