from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    name: str
    email: str
    guid: str
    password: str
    is_active: Optional[bool] = True
    created_at: Optional[datetime] = datetime.utcnow()
    updated_at: Optional[datetime] = datetime.utcnow()
    profile_picture: Optional[str] = None
    profile_cover: Optional[str] = None
    bio: Optional[str] = None
    location: Optional[str] = None
    website: Optional[str] = None
    twitter: Optional[str] = None
    github: Optional[str] = None
    linkedin: Optional[str] = None
    instagram: Optional[str] = None
    facebook: Optional[str] = None
    
    class Config:
        orm_mode = True
        from_attributes = True
from pydantic import BaseModel
from typing import Optional


class ProfileImage(BaseModel):

    id: str
    file_name: str
    path: str
    is_public: bool


class CurrentUser(BaseModel):

    id: str
    first_name: str
    last_name: str
    gender: str

    user_name: str
    mobile_no: str
    email_id: str

    profile_image: Optional[ProfileImage] = None

    class Config:
        orm_mode = True
        from_attributes = True