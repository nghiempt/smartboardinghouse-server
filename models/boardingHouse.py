from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta

boarding_house = Table(
    'boarding_house', meta,
    Column('ID', Integer, primary_key=True, autoincrement=True),
    Column('number_of_rooms', Integer),
    Column('province_city', String(255)),
    Column('district', String(255)),
    Column('ward', String(255)),
    Column('phone_number', String(255)),
    Column('accountID', Integer, ForeignKey('account.id', ondelete='CASCADE', onupdate='CASCADE'), unique=True)
)