from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Date
from config.db import meta

account_profile = Table(
    'sbh_apis_account_profile', meta,
    Column('ID', Integer, primary_key=True, autoincrement=True),
    Column('image', String(255)),
    Column('birthday', Date),
    Column('full_name', String(255)),
    Column('phone_number', String(255)),
    Column('account_ID', Integer, ForeignKey('sbh_apis_account.ID', ondelete='CASCADE'), unique=True),
)
