from pydantic import BaseModel

class Post(BaseModel):
    title: str
    content: str
    image: str
    location: str
    lat: float
    long: float
    account_id: int

    def serializeList(list):
        # Define keys for your dictionary
        keys = ['ID', 'title', 'content', 'location', 'lat', 'long', 'image', 'account_id']

        # Convert the list of tuples into a list of dictionaries
        result = [dict(zip(keys, values)) for values in list]
        return result
    
    def serializeDict(values) -> dict:
        keys = ['ID', 'title', 'content', 'location', 'lat', 'long', 'image', 'account_id']
        return dict(zip(keys, values))