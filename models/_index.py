from config.db import meta, engine
from models.account import account
from models.responseObject import ResponseObject
from models.accountProfile import account_profile
from models.transaction import transaction
from models.boardingHouse import boarding_house
from models.room import room

# Create/Update all table
meta.create_all(engine)