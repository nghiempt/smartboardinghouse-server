from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

room_image = Table(
    'room_image', meta,
    Column('room_ID', Integer, ForeignKey('room.ID', ondelete='CASCADE', onupdate='CASCADE')),
    Column('link', String(255))
)