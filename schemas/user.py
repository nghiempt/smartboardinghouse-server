from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    password: str

    def serializeList(list):
        # Define keys for your dictionary
        keys = ['id', 'name', 'email', 'password']

        # Convert the list of tuples into a list of dictionaries
        result = [dict(zip(keys, values)) for values in list]
        return result
    
    def serializeDict(values) -> dict:
        keys = ['id', 'name', 'email', 'password']
        return dict(zip(keys, values))