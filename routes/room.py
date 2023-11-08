from fastapi import APIRouter, Query
from models._index import room, account, ResponseObject
from config.db import conn
from sqlalchemy.sql import text
from schemas._index import Room, Account
import http.client as HTTP_STATUS_CODE
from starlette.responses import FileResponse


roomRouter = APIRouter(prefix="/api/v1")

@roomRouter.get('/room/detail/{ID}')
async def get_room_by_ID(ID: int):
    # Query the database to get rooms that match the specified room_ID
    room_return = conn.execute(room.select().where(room.c.ID == ID)).fetchone()

    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]

    if not room_return:
        status_code = HTTP_STATUS_CODE.NOT_FOUND
        status_message = HTTP_STATUS_CODE.responses[status_code]
        return ResponseObject(False,status_code, status_message, "No room found")

    return ResponseObject(True, status_code, status_message, Room.serializeWithAccount([room_return]))

@roomRouter.get('/room/', summary="Get rooms by house ID")
async def get_rooms_by_houseID(house_ID: int = Query(..., description="House ID to filter rooms")):
    # Query the database to get rooms that match the specified house_ID
    rooms = conn.execute(room.select().where(room.c.house_ID == house_ID)).fetchall()

    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]

    if not rooms:
        status_code = HTTP_STATUS_CODE.NOT_FOUND
        status_message = HTTP_STATUS_CODE.responses[status_code]
        return ResponseObject(False,status_code, status_message, "No rooms found")

    return ResponseObject(True, status_code, status_message, Room.serializeList(rooms))

@roomRouter.post('/room/create/empty')
async def create_room(roomInput: Room):
    # Insert the new room into the database
    conn.execute(room.insert().values(
        room_number=roomInput.room_number,
        area=roomInput.area,
        max_people=roomInput.max_people,
        status=roomInput.status,
        house_ID=roomInput.house_ID,
    ))
    conn.commit()
    status_code = HTTP_STATUS_CODE.CREATED
    status_message = HTTP_STATUS_CODE.responses[status_code]
    return ResponseObject(True, status_code, status_message, Room.serializeList(conn.execute(room.select().where(room.c.house_ID == roomInput.house_ID)).fetchall()))

@roomRouter.get('/room/contract/{ID}')
async def get_room_contract(ID: int):
    room_return = conn.execute(room.select().where(room.c.ID == ID)).fetchone()

    status_code = HTTP_STATUS_CODE.OK
    status_message = HTTP_STATUS_CODE.responses[status_code]

    if not room_return:
        status_code = HTTP_STATUS_CODE.NOT_FOUND
        status_message = HTTP_STATUS_CODE.responses[status_code]
        return ResponseObject(False,status_code, status_message, "No room found")

    # Return the PDF file as a response
    return ResponseObject(True, status_code, status_message, room_return[5])

# Function to hash the password using MD5
def md5_hash_password(password):
    return text("MD5(:password)").bindparams(password=password)

@roomRouter.post('/room/create/info')
async def register(user_credentials: Account):
    # Check if the provIDed username is already taken
    user = conn.execute(account.select().where(
        account.c.username == user_credentials.username
    )).fetchone()

    if user is not None:
        # Return an error response if the username is already taken
        status_code = HTTP_STATUS_CODE.UNAUTHORIZED
        status_message = HTTP_STATUS_CODE.responses[status_code]
        return ResponseObject(False, status_code, status_message, "Username already taken")

    # Insert the new user into the database
    conn.execute(account.insert().values(
        username=user_credentials.username,
        password=md5_hash_password(user_credentials.password),
        role=user_credentials.role,
        key=user_credentials.key,
        room_ID=user_credentials.room_ID,
    ))
    conn.commit()

    status_code = HTTP_STATUS_CODE.CREATED
    status_message = HTTP_STATUS_CODE.responses[status_code]
    return ResponseObject(True, status_code, status_message, "Sign up success")

# @roomRouter.put('/room/edit')
# async def update_room(roomInput: Room):
#     # Update the room in the database
#     conn.execute(room.update().values(
#         room_number=roomInput.room_number,
#         area=roomInput.area,
#         max_people=roomInput.max_people,
#         status=roomInput.status,
#         house_ID=roomInput.house_ID,
#     ).where(room.c.ID == roomInput.ID))
#     conn.commit()
#     status_code = HTTP_STATUS_CODE.OK
#     status_message = HTTP_STATUS_CODE.responses[status_code]
#     return ResponseObject(True, status_code, status_message, Room.serializeList(conn.execute(room.select().where(room.c.ID == roomInput.ID)).fetchall()))

# @roomRouter.delete('/room/delete')
# async def delete_room(roomInput: Room):
#     # Delete the room in the database
#     conn.execute(room.delete().where(room.c.ID == roomInput.ID))
#     conn.commit()
#     status_code = HTTP_STATUS_CODE.OK
#     status_message = HTTP_STATUS_CODE.responses[status_code]
#     return ResponseObject(True, status_code, status_message, Room.serializeList(conn.execute(room.select().where(room.c.house_ID == roomInput.house_ID)).fetchall()))


# @roomRouter.get('/room/contract')
# async def get_room_contract(room_ID: int):
#     # ProvIDe the path to the local PDF file
#     pdf_file_path = "/Users/nguyennhathung/sbh-apis/SWD392_Group01_SE1607.pdf"

#     # Return the PDF file as a response
#     return FileResponse(pdf_file_path, headers={"Content-Disposition": "inline; filename=room_contract.pdf"})



# @roomRouter.get('/room/available')
# async def get_available_rooms(house_ID: int):
#     # Query the database to get rooms that match the specified house_ID
#     rooms = conn.execute(room.select().where(room.c.house_ID == house_ID, room.c.status == 0)).fetchall()

#     status_code = HTTP_STATUS_CODE.OK
#     status_message = HTTP_STATUS_CODE.responses[status_code]

#     if not rooms:
#         status_code = HTTP_STATUS_CODE.NOT_FOUND
#         status_message = HTTP_STATUS_CODE.responses[status_code]
#         return ResponseObject(False,status_code, status_message, "No rooms found")

#     return ResponseObject(True, status_code, status_message, Room.serializeList(rooms))

# @roomRouter.get('/room/info/')
# async def get_room_info(room_ID: int):
#     # Query the database to get rooms that match the specified room_ID
#     account_return = conn.execute(account.select().where(account.c.room_ID == room_ID)).fetchone()

#     status_code = HTTP_STATUS_CODE.OK
#     status_message = HTTP_STATUS_CODE.responses[status_code]

#     if not account_return:
#         status_code = HTTP_STATUS_CODE.NOT_FOUND
#         status_message = HTTP_STATUS_CODE.responses[status_code]
#         return ResponseObject(False,status_code, status_message, "No info found")
    
#     return ResponseObject(True, status_code, status_message, Account.serializeDict(account_return))