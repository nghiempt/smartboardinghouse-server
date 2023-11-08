from pydantic import BaseModel
from models._index import room, account_profile, account
from config.db import conn

class Room(BaseModel):
    room_number: int
    area: float
    max_people: int
    status: int
    house_ID: int


    @classmethod
    def list_account(cls, room_ID):
        profile_list = []
        account_return = conn.execute(account.select().where(account.c.room_ID == room_ID)).fetchall()
        for value in account_return:
            profile_return = conn.execute(account_profile.select().where(account_profile.c.account_ID == value.ID)).fetchone()
            
            # Exclude 'birthday' field from the profile data
            profile_data = profile_return[:2] + profile_return[3:]  # Excluding index 2 (birthday)

            keys = ['ID', 'image', 'fullname', 'phone_number']
            result = dict(zip(keys, profile_data))
            profile_list.append(result)
        return profile_list
    
    def serializeList(list):
        # Define keys for your dictionary
        keys = ['ID', 'room_number', 'area', 'max_people', 'status', 'contract', 'price', 'house_ID']

        # Convert the list of tuples into a list of dictionaries
        result = [dict(zip(keys, values[:5])) for values in list]
        return result
    
    def serializeDict(values) -> dict:
        keys = ['ID', 'room_number', 'area', 'max_people', 'status', 'contract', 'price', 'house_ID']
        return dict(zip(keys, values))
    
    @classmethod
    def serializeWithAccount(cls, room_info):
        room_ID = room_info[0].ID
        room_dict = {
            'ID': room_info[0].ID,
            'room_number': room_info[0].room_number,
            'area': room_info[0].area,
            'max_people': room_info[0].max_people,
            'status': room_info[0].status,
            'contract': room_info[0].contract,
            'price': room_info[0].price,
            'house_ID': room_info[0].house_ID,
            'lodger_list': cls.list_account(room_ID)
        }
        return room_dict
