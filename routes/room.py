from fastapi import APIRouter, Query
from models._index import room, account, ResponseObject
from config.db import conn
from schemas._index import Room, Account
import http.client as HTTP_STATUS_CODE
from starlette.responses import FileResponse


roomRouter = APIRouter(prefix="/api/v1")

@roomRouter.get('/room/filter')
async def get_rooms_by_houseID(house_id: int = Query(..., description="House ID to filter rooms")):
    # Query the database to get rooms that match the specified house_id
    rooms = conn.execute(room.select().where(room.c.house_id == house_id)).fetchall()

    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]

    if not rooms:
        status_code = HTTP_STATUS_CODE.NOT_FOUND
        status_message = HTTP_STATUS_CODE.responses[status_code]
        return ResponseObject(False,status_code, status_message, "No rooms found")

    return ResponseObject(True, status_code, status_message, Room.serializeList(rooms))

@roomRouter.post('/room/create')
async def create_room(roomInput: Room):
    # Insert the new room into the database
    conn.execute(room.insert().values(
        room_number=roomInput.room_number,
        area=roomInput.area,
        max_people=roomInput.max_people,
        status=roomInput.status,
        house_id=roomInput.house_id,
    ))
    conn.commit()
    status_code = HTTP_STATUS_CODE.CREATED
    status_message = HTTP_STATUS_CODE.responses[status_code]
    return ResponseObject(True, status_code, status_message, Room.serializeList(conn.execute(room.select().where(room.c.house_id == roomInput.house_id)).fetchall()))

@roomRouter.put('/room/edit')
async def update_room(roomInput: Room):
    # Update the room in the database
    conn.execute(room.update().values(
        room_number=roomInput.room_number,
        area=roomInput.area,
        max_people=roomInput.max_people,
        status=roomInput.status,
        house_id=roomInput.house_id,
    ).where(room.c.ID == roomInput.id))
    conn.commit()
    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]
    return ResponseObject(True, status_code, status_message, Room.serializeList(conn.execute(room.select().where(room.c.ID == roomInput.id)).fetchall()))

@roomRouter.delete('/room/delete')
async def delete_room(roomInput: Room):
    # Delete the room in the database
    conn.execute(room.delete().where(room.c.ID == roomInput.id))
    conn.commit()
    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]
    return ResponseObject(True, status_code, status_message, Room.serializeList(conn.execute(room.select().where(room.c.house_id == roomInput.house_id)).fetchall()))

@roomRouter.get('/room/')
async def get_room_by_id(room_id: int):
    # Query the database to get rooms that match the specified room_id
    room_return = conn.execute(room.select().where(room.c.ID == room_id)).fetchone()

    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]

    if not room_return:
        status_code = HTTP_STATUS_CODE.NOT_FOUND
        status_message = HTTP_STATUS_CODE.responses[status_code]
        return ResponseObject(False,status_code, status_message, "No room found")

    return ResponseObject(True, status_code, status_message, Room.serializeDict(room_return))

@roomRouter.get('/room/contract')
async def get_room_contract(room_id: int):
    # Provide the path to the local PDF file
    pdf_file_path = "/Users/nguyennhathung/sbh-apis/SWD392_Group01_SE1607.pdf"

    # Return the PDF file as a response
    return FileResponse(pdf_file_path, headers={"Content-Disposition": "inline; filename=room_contract.pdf"})



@roomRouter.get('/room/available')
async def get_available_rooms(house_id: int):
    # Query the database to get rooms that match the specified house_id
    rooms = conn.execute(room.select().where(room.c.house_id == house_id, room.c.status == 0)).fetchall()

    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]

    if not rooms:
        status_code = HTTP_STATUS_CODE.NOT_FOUND
        status_message = HTTP_STATUS_CODE.responses[status_code]
        return ResponseObject(False,status_code, status_message, "No rooms found")

    return ResponseObject(True, status_code, status_message, Room.serializeList(rooms))

@roomRouter.get('/room/info/')
async def get_room_info(room_id: int):
    # Query the database to get rooms that match the specified room_id
    account_return = conn.execute(account.select().where(account.c.room_id == room_id)).fetchone()

    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]

    if not account_return:
        status_code = HTTP_STATUS_CODE.NOT_FOUND
        status_message = HTTP_STATUS_CODE.responses[status_code]
        return ResponseObject(False,status_code, status_message, "No info found")
    
    return ResponseObject(True, status_code, status_message, Account.serializeDict(account_return))