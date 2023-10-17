from pydantic import BaseModel


class Account(BaseModel):
    username: str
    password: str
    role: int
    key: str

    def serializeList(list):
        # Define keys for your dictionary
        keys = ['id', 'username', 'password', 'role', 'key']

        # Convert the list of tuples into a list of dictionaries
        result = [dict(zip(keys, values)) for values in list]
        return result
    
    def serializeDict(values) -> dict:
        keys = ['id', 'username', 'password', 'role', 'key']
        return dict(zip(keys, values))