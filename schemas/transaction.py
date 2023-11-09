from pydantic import BaseModel

class Transaction(BaseModel):
    status: int
    date: str
    content: str
    total: float
    account_ID: int

    def serializeList(list):
        # Define keys for your dictionary
        keys = ['ID', 'status', 'date', 'content', 'total', 'account_ID']

        # Convert the list of tuples into a list of dictionaries
        result = [dict(zip(keys, values)) for values in list]
        return result
    
    def serializeDict(values) -> dict:
        keys = ['ID', 'status', 'date', 'content', 'total', 'account_ID']
        return dict(zip(keys, values))