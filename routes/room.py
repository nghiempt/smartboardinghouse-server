from fastapi import APIRouter, Query
from models._index import room, ResponseObject
from config.db import conn
from schemas._index import Room
import http.client as HTTP_STATUS_CODE

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

@roomRouter.put('/room/update')
async def update_room(roomInput: Room):
    # Update the room in the database
    conn.execute(room.update().values(
        room_number=roomInput.room_number,
        area=roomInput.area,
        max_people=roomInput.max_people,
        status=roomInput.status,
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

@roomRouter.get('/room/filter/available')
async def get_available_rooms():
    # Query the database to get rooms that match the specified house_id
    # 0: Available, 1: Occupied
    rooms = conn.execute(room.select().where(room.c.status == 0)).fetchall()

    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]

    if not rooms:
        status_code = HTTP_STATUS_CODE.NOT_FOUND
        status_message = HTTP_STATUS_CODE.responses[status_code]
        return ResponseObject(False,status_code, status_message, "No rooms found")

    return ResponseObject(True, status_code, status_message, Room.serializeList(rooms))