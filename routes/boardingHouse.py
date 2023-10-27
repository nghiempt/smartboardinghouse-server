from fastapi import APIRouter, Query
from models._index import boarding_house, ResponseObject
from config.db import conn
from schemas._index import House
import http.client as HTTP_STATUS_CODE

houseRouter = APIRouter(prefix="/api/v1")

@houseRouter.get('/house/all')
async def get_all_houses():
    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]
    return ResponseObject(True, status_code, status_message, House.serializeList(conn.execute(boarding_house.select()).fetchall()))

@houseRouter.get('/house/filter')
async def get_houses_by_accountID(account_id: int = Query(..., description="Account ID to filter houses")):
    # Query the database to get houses that match the specified account_id
    houses = conn.execute(boarding_house.select().where(boarding_house.c.account_id == account_id)).fetchall()

    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]

    if not houses:
        status_code = HTTP_STATUS_CODE.NOT_FOUND
        status_message = HTTP_STATUS_CODE.responses[status_code]
        return ResponseObject(False,status_code, status_message, "No houses found")

    return ResponseObject(True, status_code, status_message, House.serializeList(houses))

@houseRouter.post('/house/create')
async def create_boarding_house(house: House):
    # Insert the new boarding house into the database
    conn.execute(boarding_house.insert().values(
        number_of_rooms=house.number_of_rooms,
        province=house.province,
        district=house.district,
        ward=house.ward,
        phone_number=house.phone_number,
        account_id=house.account_id,
    ))
    conn.commit()
    status_code = HTTP_STATUS_CODE.CREATED
    status_message = HTTP_STATUS_CODE.responses[status_code]
    return ResponseObject(True, status_code, status_message, House.serializeList(conn.execute(boarding_house.select().where(boarding_house.c.account_id == house.account_id)).fetchall()))
