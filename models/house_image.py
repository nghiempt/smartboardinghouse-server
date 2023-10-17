from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

house_image = Table(
    'house_image', meta,
    Column('boarding_house_ID', Integer, ForeignKey('boarding_house.ID', ondelete='CASCADE', onupdate='CASCADE')),
    Column('link', String(255))
)