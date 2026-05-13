from fastapi import APIRouter , Depends
from services.dependency.repo_dependecy import get_user_repository, get_current_profile
from database.database import get_db
from models.user_models import ProfileResponse, UserCreate, UserResponse

userRouter = APIRouter()

@userRouter.get("/users" , response_model=list[UserResponse] )
def list_users(db = Depends(get_db), profile: ProfileResponse = Depends(get_current_profile), limit: int = 10, offset: int = 0):
    print("Profile from auth guard:", profile.first_name)
    
    ur =get_user_repository(db)
    return ur.get_users(limit=limit, offset=offset)

# @userRouter.post("/users", response_model=UserResponse)
# def add_user(user: UserCreate,profile: ProfileResponse = Depends(get_current_profile), db = Depends(get_db) ):
#     print("Profile from auth guard:", profile.first_name)
#     ur = get_user_repository(db)
    
#     return ur.create_user(user)
