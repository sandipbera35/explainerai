from pydantic import BaseModel,ConfigDict, EmailStr
from typing import Optional
from datetime import datetime

class UserBase(BaseModel):
    name: str 
    email: EmailStr
    guid: str
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
    model_config = ConfigDict(from_attributes=True)


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    pass


User = UserCreate


from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class MediaFile(BaseModel):

    id: str
    file_name: str
    user_id: str

    size: int

    mime_type: str
    extension: str

    created_at: datetime
    updated_at: datetime

    path: str

    is_public: bool

    model_config = ConfigDict(
        from_attributes=True
    )


class ProfileResponse(BaseModel):

    id: str

    first_name: str
    last_name: str

    gender: str

    birth_date: datetime

    user_name: str

    mobile_no: str

    email_id: EmailStr

    profile_image: Optional[MediaFile] = None

    cover_image: Optional[MediaFile] = None

    model_config = ConfigDict(
        from_attributes=True
    )
