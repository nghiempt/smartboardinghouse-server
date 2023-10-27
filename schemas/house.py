from pydantic import BaseModel

class House(BaseModel):
    number_of_rooms: int
    province: str
    district: str
    ward: str
    phone_number: str
    account_id: int

    def serializeList(list):
        # Define keys for your dictionary
        keys = ['id', 'number_of_rooms', 'province', 'district', 'ward', 'phone_number', 'accountID']

        # Convert the list of tuples into a list of dictionaries
        result = [dict(zip(keys, values)) for values in list]
        return result
    
    def serializeDict(values) -> dict:
        keys = ['id', 'number_of_rooms', 'province', 'district', 'ward', 'phone_number', 'accountID']
        return dict(zip(keys, values))