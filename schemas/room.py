from pydantic import BaseModel

class Room(BaseModel):
    room_number: int
    area: float
    max_people: int
    status: int
    house_ID: int


    def serializeList(list):
        # Define keys for your dictionary
        keys = ['ID', 'room_number', 'area', 'max_people', 'status', 'house_ID']

        # Convert the list of tuples into a list of dictionaries
        result = [dict(zip(keys, values[:5])) for values in list]
        return result
    
    def serializeDict(values) -> dict:
        keys = ['ID', 'room_number', 'area', 'max_people', 'status', 'house_ID']
        return dict(zip(keys, values))