from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

room_image = Table(
    'sbh_apis_room_image', meta,
    Column('room_ID', Integer, ForeignKey('sbh_apis_room.ID', ondelete='CASCADE', onupdate='CASCADE')),
    Column('link', String(255))
)