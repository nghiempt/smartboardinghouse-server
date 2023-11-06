from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta,engine

account = Table(
    'sbh_apis_account', meta,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('username', String(255)),
    Column('password', String(255)),
    Column('role', Integer),
    Column('key', String(255)),
    Column('room_id', Integer, ForeignKey('sbh_apis_room.ID'))
)