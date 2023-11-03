from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

house_image = Table(
    'sbh_apis_house_image', meta,
    Column('house_id', Integer, ForeignKey('sbh_apis_boarding_house.ID', ondelete='CASCADE', onupdate='CASCADE')),
    Column('link', String(255))
)