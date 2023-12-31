from fastapi import APIRouter, Query
from models._index import boarding_house, ResponseObject
from config.db import conn
from schemas._index import House
import http.client as HTTP_STATUS_CODE

houseRouter = APIRouter(prefix="/api/v1")

@houseRouter.get('/house/', summary = "Get House by Account ID")
async def get_houses_by_accountID(account_ID: int = Query(..., description="Account ID to filter houses")):
    # Query the database to get houses that match the specified account_ID
    houses = conn.execute(boarding_house.select().where(boarding_house.c.account_ID == account_ID)).fetchall()

    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]

    if not houses:
        status_code = HTTP_STATUS_CODE.NOT_FOUND
        status_message = HTTP_STATUS_CODE.responses[status_code]
        return ResponseObject(False, status_code, status_message, "No houses found")

    return ResponseObject(True, status_code, status_message, House.serializeList(houses))

# @houseRouter.get('/house/all')
# async def get_all_houses():
#     status_code = HTTP_STATUS_CODE.OK
#     status_message = HTTP_STATUS_CODE.responses[status_code]
#     return ResponseObject(True, status_code, status_message, House.serializeList(conn.execute(boarding_house.select()).fetchall()))

# @houseRouter.get('/house/{ID}')
# async def get_house_by_ID(ID: int):
#     # Query the database to get houses that match the specified ID
#     house = conn.execute(boarding_house.select().where(boarding_house.c.ID == ID)).fetchall()

#     status_code = HTTP_STATUS_CODE.OK
#     status_message = HTTP_STATUS_CODE.responses[status_code]

#     if not house:
#         status_code = HTTP_STATUS_CODE.NOT_FOUND
#         status_message = HTTP_STATUS_CODE.responses[status_code]
#         return ResponseObject(False,status_code, status_message, "No houses found")

#     return ResponseObject(True, status_code, status_message, House.serializeList(house))

# @houseRouter.put('/house/{ID}')
# async def update_boarding_house(ID: int, house: House):
#     # Update the boarding house in the database
#     conn.execute(boarding_house.update().values(
#         number_of_rooms=house.number_of_rooms,
#         name=house.name,
#         province=house.province,
#         district=house.district,
#         ward=house.ward,
#         price=house.price,
#         phone_number=house.phone_number,
#     ).where(boarding_house.c.ID == ID))
#     conn.commit()
#     status_code = HTTP_STATUS_CODE.OK
#     status_message = HTTP_STATUS_CODE.responses[status_code]
#     return ResponseObject(True, status_code, status_message, House.serializeList(conn.execute(boarding_house.select().where(boarding_house.c.ID == ID)).fetchall()))

# @houseRouter.post('/house/create')
# async def create_boarding_house(house: House):
#     # Insert the new boarding house into the database
#     conn.execute(boarding_house.insert().values(
#         number_of_rooms=house.number_of_rooms,
#         name=house.name,
#         province=house.province,
#         district=house.district,
#         ward=house.ward,
#         price=house.price,
#         phone_number=house.phone_number,
#         account_ID=house.account_ID,
#     ))
#     conn.commit()
#     status_code = HTTP_STATUS_CODE.CREATED
#     status_message = HTTP_STATUS_CODE.responses[status_code]
#     return ResponseObject(True, status_code, status_message, House.serializeList(conn.execute(boarding_house.select().where(boarding_house.c.account_ID == house.account_ID)).fetchall()))

# @houseRouter.get('/house/group_message')
# async def get_house_by_group_message():
#         list = []
#         return ResponseObject(True, 200, "OK", list)
