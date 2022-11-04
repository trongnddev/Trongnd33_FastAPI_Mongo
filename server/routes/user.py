from re import A
from fastapi  import APIRouter

from  models.user import User
from config.database import client

user = APIRouter

# @user.get('/')
# async def get_all_user():
#     return client.