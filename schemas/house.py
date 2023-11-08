from pydantic import BaseModel
from sqlalchemy import func, select
from config.db import conn
from models._index import room, house_image

class House(BaseModel):
    number_of_rooms: int
    lat: str
    lng: str
    name: str
    price: int
    province: str
    district: str
    ward: str
    phone_number: str
    account_ID: int
    number_of_rooms_available: int

    @classmethod
    def count_room(cls, house_ID):
        count = 0
        room_return = conn.execute(room.select().where(room.c.house_ID == house_ID)).fetchall()
        for row in room_return:
            if row.status == 0:
                count += 1
        return count

    @classmethod
    def list_image(cls, house_ID):
        image_list = []
        image_return = conn.execute(house_image.select().where(house_image.c.house_ID == house_ID)).fetchall()
        for row in image_return:
            image_list.append(row.link)
        return image_list

    @classmethod
    def serializeList(cls, house_list):
        result = []
        for house in house_list:
            number_of_rooms_available = cls.count_room(house[0])
            images = cls.list_image(house[0])
            house_dict = {
                'ID': house[0],
                'name': house[1],
                'number_of_rooms': house[2],
                'number_of_rooms_available': number_of_rooms_available,
                'house_image': images,
                'lat': house[3],
                'lng': house[4],
                'province': house[5],
                'district': house[6],
                'ward': house[7],
                'phone_number': house[8],
                'price': house[9],
                'account_ID': house[10]
            }
            result.append(house_dict)

        return {'list_of_house': result, 'number_of_house': len(house_list)}
