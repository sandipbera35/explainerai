from anyio import current_time
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database.schemas.users import User
from models.user_models import User as UserRequest



async def create_user(
    db: AsyncSession,
    user_data: UserRequest
    #current_time_utc
    
):
    timeNow = current_time()

    user = User(
        created_at=timeNow,
        updated_at=timeNow,
        is_active=user_data.is_active,
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

    db.add(user)

    await db.commit()

    await db.refresh(user)

    return user


async def get_users(
    db: AsyncSession
):

    result = await db.execute(
        select(User)
    )

    users = result.scalars().all()

    return users

async def get_user_by_userid(
    db: AsyncSession,
    user_id: str
):

    result = await db.execute(
        select(User).where(User.id == user_id)
    )

    user = result.scalar_one_or_none()

    return user