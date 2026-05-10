from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer
from fastapi import Depends

from database.database import get_db
from models.user_models import CurrentUser, User as UserRequest, CurrentUser
from services.user_repo import get_users , create_user , get_user_by_userid


import httpx    
from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials
)

security = HTTPBearer()

AUTH_SERVICE_URL = "http://localhost:8080/api/v1/profile"


async def auth_guard(
    request: Request,
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> CurrentUser :
    
    request.state.db = await get_db().__anext__()
    db = request.state.db


    auth_header = request.headers.get(
        "Authorization"
    )
    
    if not auth_header:

        raise HTTPException(
            status_code=401,
            detail="Authorization header missing"
        )

    async with httpx.AsyncClient() as client:
        # remove bearer from auth header
        auth_header = auth_header.replace("Bearer ", "")
        
        print("Auth header:", auth_header)

        response = await client.get(
            AUTH_SERVICE_URL,
            headers={
                "Authorization": auth_header
            }
        )
    print("Auth service response status:", response.json())
    if response.status_code != 200:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
    else:
        user = response.json()
        user = CurrentUser(**user)
        userchk = await get_user_by_userid(db, user_id=user.id)
       
        if not userchk:
            db_user = UserRequest(
                guid = user.id,             
                name = user.first_name + " " + user.last_name,
          
                email = user.email_id,
                password = "hashed_password",
                profile_picture = user.profile_image.path if user.profile_image else None,
                # profile_cover = user.pr,
                # bio = user.bio,
                # location = user.location,
                # website = user.website,
                # twitter = user.twitter,
                # github = user.github,
                # linkedin = user.linkedin,
                # instagram = user.instagram,
                # facebook = user.facebook
            )
            await create_user(db, db_user)
            request.state.user = user
            return user
        else:
            request.state.user = user
            return user