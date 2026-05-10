from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

import httpx


security = HTTPBearer()

AUTH_SERVICE_URL = "http://localhost:8080/api/v1/profile"


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):

    token = credentials.credentials

    headers = {
        "Authorization": f"Bearer {token}"
    }

    async with httpx.AsyncClient() as client:

        response = await client.get(
            AUTH_SERVICE_URL,
            headers=headers
        )

    if response.status_code != 200:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    return response.json()