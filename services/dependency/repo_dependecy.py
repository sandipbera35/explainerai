from fastapi import Depends
from sqlalchemy.orm import Session

from database.database import get_db
from services.repositories.user_repo import UserRepository
from services.repositories.auth_repo import AuthRepository
from services.repositories.ai_repo import OllamaClient, OllamaConfig
from models.user_models import ProfileResponse


def get_user_repository(
    db: Session = Depends(get_db)
):

    return UserRepository(db)

def get_auth_repository(db: Session = Depends(get_db)):
    return AuthRepository(db)


def get_current_profile(
    auth_repository: AuthRepository = Depends(get_auth_repository),
) -> ProfileResponse:
    return auth_repository.get_profile()

def get_ai_repository():
    
    return OllamaClient(
        config=OllamaConfig(
            model_name="gemma4:e4b"
        )
    )
