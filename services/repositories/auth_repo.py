

from fastapi import HTTPException
import httpx

from models.user_models import ProfileResponse
from models.user_models import UserCreate
from services.repositories.user_repo import UserRepository
from pydantic import UUID4



class AuthRepository:
    token = None
    def __init__(self, db):
        self.db = db
    #return access token from auth service
    
    def get_token(self) -> str:
        print("Getting token from auth service...")
        login_url = "http://localhost:8080/api/v1/login"
        with httpx.Client() as client:
            response =  client.post(
                login_url,
                json={
                    "email_id": "sandipbera35@outlook.com",
                    "password": "MYPASS"
                },
            )
        if response.status_code != 200:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )
        else:
            data = response.json()
            token = data.get("access_token")
            if not token:
                raise HTTPException(
                    status_code=401,
                    detail="Token not found in response"
                )
            else:
                self.token = token
                print("Token obtained from auth service:", token)
                return token
            
    def get_profile(self) -> ProfileResponse :
        self.get_token()
        profile_url = "http://localhost:8080/api/v1/profile"
        with httpx.Client() as client:
            profile_response = client.get(
                profile_url,
                headers={
                    "Authorization": f"{self.token}"
                }
            )
        if profile_response.status_code != 200:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )
        else:
            user = ProfileResponse(**profile_response.json())
            print("Profile from auth service:", user)
            ur = UserRepository(self.db)
            db_user = ur.get_user_by_userid(user_id=user.id)
            
            if not db_user:
                
                create_user_data = UserCreate(
                    guid=user.id,
                    name=f"{user.first_name} {user.last_name}",
                    email= f"{user.email_id.lower()}",
                    password="MYPASS",
                    is_active=True,
                    profile_picture=user.profile_image.path if user.profile_image else None,
                    profile_cover=user.cover_image.path if user.cover_image else None,
                    bio=None,
                    location=None,
                    website=None,
                    twitter=None,
                    github=None,
                    linkedin=None,
                    instagram=None,
                    facebook=None,  
                    
                    
                )
                ur.create_user(user_data=create_user_data)
            return user
            
                
                
