from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Date, Float
from config.db import meta, engine

transaction = Table(
    'sbh_apis_transaction', meta,
    Column('ID', Integer, primary_key=True, autoincrement=True),
    Column('status', Integer),
    Column('date', Date),
    Column('type', String(255)),
    Column('total', Float),
    Column('account_profile_ID', Integer, ForeignKey('sbh_apis_account_profile.id', onupdate='CASCADE'))
)