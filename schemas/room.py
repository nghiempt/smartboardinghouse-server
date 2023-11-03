from pydantic import BaseModel

class Room(BaseModel):
    room_number: int
    area: float
    max_people: int
    status: int
    house_id: int


    def serializeList(list):
        # Define keys for your dictionary
        keys = ['ID', 'room_number', 'area', 'max_people', 'status', 'house_id']

        # Convert the list of tuples into a list of dictionaries
        result = [dict(zip(keys, values)) for values in list]
        return result
    
    def serializeDict(values) -> dict:
        keys = ['ID', 'room_number', 'area', 'max_people', 'status', 'house_id']
        return dict(zip(keys, values))