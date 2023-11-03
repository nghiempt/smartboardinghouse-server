from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Float
from config.db import meta

room = Table(
    'sbh_apis_room', meta,
    Column('ID', Integer, primary_key=True, autoincrement=True),
    Column('room_number', Integer),
    Column('area', Float),
    Column('max_people', Integer),
    Column('status', Integer),
    Column('house_id', Integer, ForeignKey('sbh_apis_boarding_house.ID'))
)
