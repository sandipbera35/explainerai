from fastapi import APIRouter , Depends
from auth.auth_gourd import auth_guard
from database.database import get_db

userRouter = APIRouter()

from services.user_repo import create_user, get_users
from models.user_models import User
from models.user_models import User as UserRequest , CurrentUser



@userRouter.get("/users")
async def list_users(db = Depends(get_db), profile: CurrentUser = Depends(auth_guard), limit: int = 10, offset: int = 0):
    
    print("Profile from auth guard:", profile)
    return await get_users(db)

@userRouter.post("/users")
async def add_user(user: UserRequest,profile = Depends(auth_guard), db = Depends(get_db) ):
    print("Profile from auth guard:", profile)
    return await create_user(db, user)
