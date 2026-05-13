from fastapi import APIRouter , Depends

from services.dependency.repo_dependecy import get_user_repository, get_current_profile
from database.database import get_db
from models.user_models import ProfileResponse, UserCreate, UserResponse

from services.dependency.repo_dependecy import get_ai_repository

ollama = get_ai_repository()



aiRouter = APIRouter()

@aiRouter.post("/explain")
def explain_code(
    prompt: str
):

    result =  ollama.explain_code(
        prompt
    )

    return {
        "response": result
    }

