from pydantic import BaseModel


class Account(BaseModel):
    username: str
    password: str
    role: int
    key: str
    room_ID: int

    def serializeList(list):
        # Define keys for your dictionary
        keys = ['ID', 'username', 'password', 'role', 'key', 'room_ID']

        # Convert the list of tuples into a list of dictionaries
        result = [dict(zip(keys, values)) for values in list]
        return result
    
    def serializeDict(values) -> dict:
        keys = ['ID', 'username', 'password', 'role', 'key', 'room_ID']
        return dict(zip(keys, values))