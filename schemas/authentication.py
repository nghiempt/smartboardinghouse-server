from pydantic import BaseModel


class Login(BaseModel):
    username: str
    password: str

    def serializeDict(values) -> dict:
        keys = ['role', 'account_ID']
        return dict(zip(keys, values))