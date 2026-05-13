
from sqlalchemy import select
from sqlalchemy.orm import Session

from fastapi import Depends
from database.schemas.users import User
from models.user_models import UserCreate
from database.database import get_db

from datetime import datetime


class UserRepository:
    def __init__(self, db: Session = Depends(get_db)):
        self.db = db
        
    def get_user_by_userid(
    self,
    user_id: str,
    ) -> User | None:

        query = select(User).where(User.guid == user_id)

        result = self.db.execute(query)

        user = result.scalars().first()

        return user
    def get_users(
        self,
        limit: int = 10,
        offset: int = 0,
    ):

        result = self.db.execute(
            select(User).limit(limit).offset(offset)
        )

        users = result.scalars().all()
        
        if not users:
            return []
        return users
    def create_user(
        self,
        user_data: UserCreate
    ) -> User:
        timeNow = datetime.utcnow()

        user = User(
            created_at=timeNow,
            updated_at=timeNow,
            is_active=user_data.is_active,
            guid=user_data.guid,
            name=user_data.name,
            email=user_data.email,
            password=user_data.password,
            profile_picture=user_data.profile_picture,
            profile_cover=user_data.profile_cover,
            bio=user_data.bio,
            location=user_data.location,
            website=user_data.website,
            twitter=user_data.twitter,
            github=user_data.github,
            linkedin=user_data.linkedin,
            instagram=user_data.instagram,
            facebook=user_data.facebook,
        )
        
        try:
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
        except Exception as e:
            self.db.rollback()
            raise e
        return user
    
    def current_time(self):
        timeNow = datetime.utcnow()
        return timeNow
    
    
