
from typing import Optional, List
from pydantic import BaseModel

class AnonymousUserModel(BaseModel):
    is_authenticated: bool = True
    username: str = "Anonymous"
    email: str = None
    id: int = None

class CustomerModel(AnonymousUserModel):
    user_number: str = None
    current_balance : float = None

class UserModel(BaseModel):
    id: int
    last_login: Optional[str]
    is_superuser: bool
    first_name: Optional[str] = ""
    last_name: Optional[str] = ""
    is_staff: bool
    date_joined: str
    n_id: int
    username: str
    email: str
    password: str
    account_no: str
    phone_no: str
    balance: float
    is_active: bool
    joining_date: str
    groups: List[str] = []
    user_permissions: List[str] = []


