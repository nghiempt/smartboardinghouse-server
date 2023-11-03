from sqlalchemy import create_engine, MetaData

# engine = create_engine(
#     "mysql+pymysql://sbh:Sbh123@143.198.223.56/phpmyadmin", echo=True)
engine = create_engine(
    "mysql+pymysql://root@localhost:3306/sbh_apis", echo=True)
meta = MetaData()
conn = engine.connect()