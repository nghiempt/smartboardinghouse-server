from pydantic import BaseModel

class Transaction(BaseModel):
    status: int
    date: str
    type: str
    total: float
    account_profile_ID: int

    def serializeList(list):
        # Define keys for your dictionary
        keys = ['ID', 'status', 'date', 'type', 'total', 'account_profile_ID']

        # Convert the list of tuples into a list of dictionaries
        result = [dict(zip(keys, values)) for values in list]
        return result
    
    def serializeDict(values) -> dict:
        keys = ['ID', 'status', 'date', 'type', 'total', 'account_profile_ID']
        return dict(zip(keys, values))