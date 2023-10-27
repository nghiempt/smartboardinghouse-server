from sqlalchemy import create_engine, MetaData

# engine = create_engine(
#     "mysql+pymysql://root:nu7jrc_910471fmt1tqa9g3n-rpq740n@viaduct.proxy.rlwy.net:11824/railway", echo=True)
engine = create_engine(
    "mysql+pymysql://root@localhost:3306/fastapi_mysql", echo=True)
meta = MetaData()
conn = engine.connect()